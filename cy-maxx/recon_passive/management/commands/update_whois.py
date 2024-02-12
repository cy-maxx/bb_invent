# your_app/management/commands/update_whois.py

from django.core.management.base import BaseCommand
from recon_passive.utils import save_whois_information

class Command(BaseCommand):
    help = 'Update whois information for a given domain'

    def add_arguments(self, parser):
        parser.add_argument('domain_name', type=str, help='Domain name to update whois information')

    def handle(self, *args, **kwargs):
        domain_name = kwargs['domain_name']
        save_whois_information(domain_name)
