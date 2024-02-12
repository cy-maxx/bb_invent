import whois
from datetime import datetime
from .models import WhoisInformation

def save_whois_information(domain_name):
    
    try:
        # Retrieve whois information using python-whois library
        domain_info = whois.whois(domain_name)

        # Create a WhoisInformation instance
        whois_instance, created = WhoisInformation.objects.get_or_create(
            domain_name=domain_name,
            defaults={
                'registrar': domain_info.registrar,
                'creation_date': domain_info.creation_date,
                'expiration_date': domain_info.expiration_date,
                'updated_date': domain_info.updated_date,
                'registrant_name': domain_info.registrant_name,
                'registrant_email': domain_info.registrant_email,
                'nameservers': ', '.join(domain_info.name_servers),
                'raw_data': str(domain_info),
            }
        )

        if not created:
            # Update existing instance if it already exists
            whois_instance.registrar = domain_info.registrar
            whois_instance.creation_date = domain_info.creation_date
            whois_instance.expiration_date = domain_info.expiration_date
            whois_instance.updated_date = domain_info.updated_date
            whois_instance.registrant_name = domain_info.registrant_name
            whois_instance.registrant_email = domain_info.registrant_email
            whois_instance.nameservers = ', '.join(domain_info.name_servers)
            whois_instance.raw_data = str(domain_info)

            whois_instance.save()

        print(f"Whois information for {domain_name} saved successfully.")
    except Exception as e:
        print(f"Error saving whois information for {domain_name}: {e}")

