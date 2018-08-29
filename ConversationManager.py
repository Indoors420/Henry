# Usage:
#   Create a conversation with `add`
#   Check if a conversation exists with `is_conversing_with`
#   To tell the system that a message has ben responded with, call `update`

import time, discord


class ConversationManager:
    conversations = []
    conversationTimes = {}
    timeout = 10.0

    def __init__(self, timeout=10.0):
        self.timeout = timeout

    def remove_stale_conversations(self) -> None:
        for user_id, conversationTime in self.conversationTimes.items():
            if time.time() - conversationTime> self.timeout:
                if user_id in self.conversations:
                    self.conversations.remove(user_id)
                self.conversationTimes[user_id] = None
        self.conversationTimes = {k: v for k, v in self.conversationTimes.items() if v is not None}

    def add(self, user: discord.User) -> None:
        self.remove_stale_conversations()
        if user.id not in self.conversations:
            self.conversations.append(user.id)
            self.conversationTimes[user.id] = time.time()
        else:
            self.conversationTimes[user.id] = time.time()

    def remove(self, user: discord.User) -> None:
        self.remove_stale_conversations()
        if user.id in self.conversations: self.conversations.remove(user.id)

    def conversing_with(self, user: discord.User) -> bool:
        self.remove_stale_conversations()
        return user.id in self.conversations

    def update(self, user: discord.User) -> None:
        if user.id in self.conversations: self.conversationTimes[user.id] = time.time()
        self.remove_stale_conversations()
