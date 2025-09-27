import os
import sys
import django
import json
from django.utils.dateparse import parse_datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from comments.models import Comment

def load_comments():
    Comment.objects.all().delete()
    
    with open('../comments_data.json', 'r') as f:
        data = json.load(f)
    
    for comment_data in data['comments']:
        date = parse_datetime(comment_data['date'])
        image_data = {'url': comment_data['image']} if comment_data.get('image') else {}
        
        Comment.objects.create(
            author=comment_data['author'],
            text=comment_data['text'],
            created_at=date,
            likes=comment_data['likes'],
            image=image_data
        )
    
    print(f'Loaded {len(data["comments"])} comments')

if __name__ == '__main__':
    load_comments()
