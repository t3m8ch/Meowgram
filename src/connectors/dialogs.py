from meowgram.backend.telegram_client import client
from meowgram.backend.asyncio_separator import aio


class DialogsManager:
    def show_dialogs(self, done_callback):
        future = aio.run(client.get_dialogs, ())
        future.add_done_callback(done_callback)
        return future

        # window.update_contacts_listbox(dialogs)

dialogs_manager = DialogsManager()
