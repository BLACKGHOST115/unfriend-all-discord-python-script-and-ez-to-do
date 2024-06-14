
import discum

# Replace with your Discord account token
TOKEN = 'YOUR_DISCORD_TOKEN'

# Initialize the client
client = discum.Client(token=TOKEN, log=False)

@client.gateway.command
def on_ready(resp):
    if client.gateway.session_id:  # Check if the client is ready
        client.gateway.removeCommand(on_ready)
        print('Bot is ready.')

        # Fetch the list of relationships (friends)
        relationships = client.getRelationships()

        # Unfriend each friend
        for relationship in relationships.json():
            if relationship['type'] == 1:  # Type 1 indicates a friend
                friend_id = relationship['id']
                client.removeRelationship(friend_id)
                print(f'Unfriended {friend_id}')
        client.gateway.close()

# Run the gateway to start the bot
client.gateway.run()