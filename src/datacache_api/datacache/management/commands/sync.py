from django.core.management.base import BaseCommand
from datacache.models import UnSyncWallet, sync_tags

class Command(BaseCommand):
    help = 'Sync tags of wallet'

    def handle(self, *args, **kwargs):
        print("Sync")
        query = UnSyncWallet.objects.all()
        for cell in query:
            sync_tags(cell.wallet_address)
            cell.delete()
