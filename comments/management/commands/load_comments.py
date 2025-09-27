import json
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime
from comments.models import Comment

class Command(BaseCommand):
    help = 'Load comments from JSON file'

    def handle(self, *args, **options):
        # Clear existing comments
        Comment.objects.all().delete()
        
        # Load comments from JSON file
        with open('comments_data.json', 'r') as f:
            data = json.load(f)
        
        comments_created = 0
        for comment_data in data['comments']:
            # Parse the date
            date = parse_datetime(comment_data['date'])
            
            # Create image data
            image_data = {}
            if comment_data.get('image'):
                image_data = {'url': comment_data['image']}
            
            # Create comment
            comment = Comment.objects.create(
                author=comment_data['author'],
                text=comment_data['text'],
                created_at=date,
                likes=comment_data['likes'],
                image=image_data
            )
            comments_created += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully loaded {comments_created} comments')
        )