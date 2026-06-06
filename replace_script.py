import re

with open('/home/jules/vidspark-site/channels.html', 'r') as f:
    content = f.read()

search_block = """        // Permettre à l'utilisateur d'entrer son Channel ID manuellement
        // Format: UC + 22 caractères alphanumériques
        // Exemple: UCxxxxxxxxxxxxxxxxxxxxx
        const channelIdInput = document.querySelector('#channelSelect') || document.querySelector('#channelsGrid');
        if (channelIdInput) {
          // Mode simple: ajouter un input au lieu du dropdown
          if (currentUserPlan !== 'business') {
            const container = document.querySelector('.form-group');
            if (container) {
              container.innerHTML = `
                <label for="manualChannelId">ID de votre chaîne YouTube:</label>
                <input id="manualChannelId" type="text" placeholder="ex: UCxxxxxxxxxxxxxxxxxxxxx" style="width: 100%; padding: 12px 14px; background: #1a1a20; color: #e8e8f0; border: 1px solid #2a2a35; border-radius: 8px; font-size: 14px;">
                <p style="font-size: 12px; color: #8888a0; margin-top: 8px;">
                  👉 <strong>Comment trouver votre Channel ID?</strong><br>
                  1. Allez sur votre chaîne YouTube<br>
                  2. Cliquez sur l'URL: youtube.com/channel/<strong>UCxxxxxxxxxxxxxxxxxxxxx</strong><br>
                  3. Copiez la partie <strong>UC...</strong> (commence par UC + 22 caractères)
                </p>
              `;
            }
          }
        }

        availableChannels = [];"""

replace_block = """        // Charger les chaines selectionnees depuis le backend
        const channelsRes = await fetch(`${BACKEND_URL}/channels/list`, {
          headers: { 'Authorization': `Bearer ${token}` }
        });
        const channelsData = await channelsRes.json();

        if (channelsData.success && channelsData.data && channelsData.data.length > 0) {
           showError('Vous avez déjà configuré vos chaînes. Le choix est définitif. Redirection vers le tableau de bord...');
           setTimeout(() => { window.location.href = '/dashboard.html'; }, 3000);
           return;
        }

        // Pour l'instant on garde le champ manuel (ou dropdown si YouTube API était connectée)
        availableChannels = [];"""

if search_block in content:
    content = content.replace(search_block, replace_block)
    with open('/home/jules/vidspark-site/channels.html', 'w') as f:
        f.write(content)
    print("Replaced successfully")
else:
    print("Search block not found")
