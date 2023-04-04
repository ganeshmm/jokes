from flask import Flask, render_template, request
import heapq
import torch
from transformers import DistilBertTokenizer

app = Flask(__name__)

model = torch.load('../models/model-2.pth', map_location=torch.device('cpu'))
model.eval()

tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased', use_fast=True)

heap = list()
MAX_HEAP_SIZE = 3

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/laugh', methods=['POST'])
def laugh():
    joke = request.form['joke'].replace('\n', ' ')
    laughter = get_laughter(joke)
    add_to_heap(joke, laughter)
    emoji, favicon = choose_emoji(laughter)
    return render_template('index.html', 
                           laughter=laughter, 
                           heap=sorted(heap, reverse=True), 
                           emoji=emoji,
                           favicon=favicon,
                           prev_joke=joke)

def get_laughter(joke):
    encoded_joke = tokenizer(joke, return_tensors='pt')
    laughter = model(**encoded_joke).logits.item()
    return laughter

def add_to_heap(joke, laughter):
    if len(heap) < MAX_HEAP_SIZE:
        heapq.heappush(heap, (laughter, joke))
    else:
        heapq.heappushpop(heap, (laughter, joke))

def choose_emoji(laughter):
    if laughter < 1.0:
        return '\U0001F610', 'neutral' # neutral face
    elif laughter < 2.0:
        return '\U0001F642', 'smile' # slightly smiling face
    elif laughter < 3.0:
        return '\U0001F601', 'beaming' # beaming face with smiling eyes
    elif laughter < 4.0:
        return '\U0001F602', 'tears' # face with tears of joy
    else:
        return '\U0001F923', 'rofl' # rolling on the floor laughing