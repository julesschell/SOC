1. Identification et Analyse de l'Incident

La première étape du processus consiste à identifier et analyser l'incident. Lorsque l'infrastructure de surveillance, telle que Splunk ou Sigma, détecte une activité suspecte ou un potentiel incident, il est crucial d'évaluer rapidement la situation. Cette évaluation inclut la classification de l’incident selon sa criticité (faible, moyenne, élevée ou critique). Cette classification est essentielle pour définir le degré d’urgence de la réponse et le délai de notification. Plus l’incident est grave, plus la rapidité de la réaction devient primordiale pour limiter les impacts sur les infrastructures et les données du client. Il est impératif d'identifié si cette incident est un faux positif également pour ne pas notifier le clients d'un activité légitime.

2. Notification Initiale au Client

Dès qu’un incident est identifié, une notification initiale doit être envoyée au client dans un délai maximum de deux heures pour les incidents critiques ou de haute priorité. Cette notification, même si elle reste préliminaire, permet au client de se préparer et de prendre les premières mesures si nécessaire. Le contenu de cette notification doit inclure une brève description de l’incident, son impact potentiel et l’état de l’investigation (en cours). Le canal privilégié pour cette communication est l’e-mail, mais en cas de criticité extrême, il peut être préférable de contacter le client par téléphone afin de s’assurer qu’il prend connaissance de l’incident rapidement.

3. Qualification et Rapport d'Investigation Préliminaire

Une fois l'incident signalé, l'équipe procède à une qualification plus approfondie dans un délai de quatre heures. Cette qualification se matérialise par un rapport d’investigation préliminaire, qui apporte des détails plus précis sur la nature de l’incident et ses implications. Ce document comprend une analyse initiale, des hypothèses sur la cause potentielle de l’incident et des recommandations pour des actions immédiates de remédiation. L’envoi de ce rapport permet au client de mieux comprendre la situation et de mettre en place les premières actions correctives pour limiter les risques. Pour assurer une traçabilité optimale, l’objet de l’e-mail suit une nomenclature spécifique (cf Présentation du projet).

4. Mise à Jour et Rapport Final

Dans un délai de 72 heures, un rapport d’investigation final doit être envoyé pour documenter l'ensemble des actions réalisées et des observations faites, incluant des recommandations moyen terme pour renforcer la sécurité. Ce rapport final est essentiel, car il fournit une vision exhaustive de l’incident, aide le client à évaluer les risques résiduels, et lui permet d’ajuster ses procédures de sécurité en fonction des vulnérabilités identifiées.

5. Automatisation et Surveillance Continue

Pour accéléré le processus de réponse à incident, nous avons mis en place un algorithme nous permettant de récupérer les nouvelles alertes non traitées. Grâce a celui-ci nous pourrons rapidement notifier le client et lui permettre de répondre plus rapidement a l'incident.