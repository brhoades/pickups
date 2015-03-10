"""Utility functions."""

from hangups.ui.utils import get_conv_name
import hashlib
import re

def conversation_to_channel(conv):
    """Return channel name for hangups.Conversation."""
    # Must be 50 characters max and not contain space or comma.
    name = get_conv_name(conv).replace(',', '').replace(' ', '_')
    return '#{}'.format(name[:50 - 3])


def channel_to_conversation(channel, conv_list):
    """Return hangups.Conversation for channel name."""
    for conv in conv_list.get_all():
        if ''.join( [ '#', get_conv_name(conv).replace(',', '').replace( ' ', '_' ) ] ) == channel:
            return conv 
    else:
        return None


def get_nick(user):
    """Return nickname for a hangups.User."""
    # Remove disallowed characters and limit to max length 15
    return re.sub(r'[^\w\[\]\{\}\^`|_\\-]', '', user.full_name)[:15]


def get_hostmask(user):
    """Return hostmask for a hangups.User."""
    return '{}!{}@hangouts'.format(get_nick(user), user.id_.chat_id)


def get_topic(conv):
    """Return IRC topic for a conversation."""
    if conv == None:
        return "Unknown"
    return 'Hangouts conversation: {}'.format(get_conv_name(conv))
