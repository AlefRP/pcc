import sandwiches
from display import display_message, favorite_book
from  user_profile_v2 import build_profile as bp
import pets_v3 as pt 

sandwiches.make_sandwich('cheese', 'ham', 'bacon')
display_message()
favorite_book('the hobbit')
bp('john', 'doe', location='new york', field='computer science')
pt.describe_pet('dog', 'fido')