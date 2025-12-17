# projet-sae502
deploiement automatisé d'une plateforme de supervision basée sur Docker et Ansible

sur le /home/rt j'ai crée aussi le dossier backend et frontend:

Docker Compose essaie de builder l’image backend depuis ./backend

Ansible a copié docker-compose.yml dans /home/rt/

Mais le dossier backend n’existe pas dans /home/rt/

Donc Docker Compose ne trouve pas le contexte pour build

Raison : quand Ansible copie docker-compose.yml dans /home/{{ ansible_user }}/docker-compose.yml, il faut aussi copier le dossier backend complet.


j'ai eu un probleme cr j'avais modifé mon fichier readme sur guithub et il y'a eu des conflits en faisaint git push --> pour résoudre: git pull origin main --rebase
