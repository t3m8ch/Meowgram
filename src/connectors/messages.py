from meowgram.backend.telegram_client import client
from meowgram.backend.asyncio_separator import aio
import concurrent.futures


class MessagesManager:

    loaded_chat_id = []
    loaded_messages = []

    def show_messages(self, chat_id, done_callback):
        print(chat_id)

        actual_chat_id = self._get_actual_id(chat_id)

        if actual_chat_id not in self.loaded_chat_id:
            future = aio.run(client.get_messages, (chat_id,))
            future.add_done_callback(done_callback)
            return future
        else:
            # Creating fake future
            future = concurrent.futures.Future()
            future.done()
            index = self.loaded_chat_id.index(actual_chat_id)
            messages = self.loaded_messages[index]
            future._result = messages
            add_done_callback(future)
            return future

            # self.loaded_chat_id.append(actual_chat_id)
            # self.loaded_messages.append(messages)

        # else:
        #     index = self.loaded_chat_id.index(actual_chat_id)
        #     messages = self.loaded_messages[index]

        # window.update_messages_listbox(messages)

    def _get_actual_id(self, chat_id):
        if hasattr(chat_id, 'channel_id'):
            actual_id = chat_id.channel_id
        else:
            actual_id = chat_id.user_id
        return actual_id

messages_manager = MessagesManager()
