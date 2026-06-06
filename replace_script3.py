with open('/home/jules/vidspark-site/channels.html', 'r') as f:
    content = f.read()

search_block = """    async function submitSimpleMode() {
      // Essayer d'abord le input manuel
      let channelId = document.getElementById('manualChannelId')?.value;
      let channelName = 'Ma Chaîne YouTube';

      // Si pas d'input manuel, utiliser le dropdown
      if (!channelId) {
        const select = document.getElementById('channelSelect');
        channelId = select?.value;
        const selectedOption = select?.options[select.selectedIndex];
        channelName = selectedOption?.dataset.name || 'Chaîne';
      }

      if (!channelId || !channelId.match(/^UC[a-zA-Z0-9_-]{22}$/)) {
        showError('Channel ID invalide. Format: UCxxxxxxxxxxxxxxxxxxxxx (UC + 22 caractères)');
        return;
      }

      await submitChannelSelection([{ id: channelId, name: channelName }]);
    }"""

replace_block = """    async function submitSimpleMode() {
      let channelId = document.getElementById('channelSelect')?.value;
      const select = document.getElementById('channelSelect');
      const selectedOption = select?.options[select.selectedIndex];
      let channelName = selectedOption?.dataset.name || 'Chaîne';

      // Fallback à l'input manuel s'il existe (pour le moment car la liste n'est pas encore tirée de Google API)
      if (!channelId || channelId === '') {
         channelId = document.getElementById('manualChannelId')?.value;
         channelName = 'Ma Chaîne YouTube';
      }

      if (!channelId || !channelId.match(/^UC[a-zA-Z0-9_-]{22}$/)) {
        showError('Channel ID invalide. Format: UCxxxxxxxxxxxxxxxxxxxxx (UC + 22 caractères)');
        return;
      }

      await submitChannelSelection([{ id: channelId, name: channelName }]);
    }"""

if search_block in content:
    content = content.replace(search_block, replace_block)
    with open('/home/jules/vidspark-site/channels.html', 'w') as f:
        f.write(content)
    print("Replaced successfully")
else:
    print("Search block not found")
