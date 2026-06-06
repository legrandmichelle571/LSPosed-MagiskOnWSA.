with open('/home/jules/vidspark-site/channels.html', 'r') as f:
    content = f.read()

search_block = """          body: JSON.stringify({
            channels: channels.map(ch => ({
              youtube_channel_id: ch.id,
              channel_name: ch.name
            }))
          })"""

replace_block = """          body: JSON.stringify({
            channels: channels.map(ch => ({
              youtube_channel_id: ch.id,
              channel_name: ch.name || 'Ma Chaine'
            }))
          })"""

if search_block in content:
    content = content.replace(search_block, replace_block)
    with open('/home/jules/vidspark-site/channels.html', 'w') as f:
        f.write(content)
    print("Replaced successfully")
else:
    print("Search block not found")
