+++
title = "Winterprojekte"
date = 2023-02-09

[taxonomies]
categories = ["german"]
tags = ["german", "annoucement"]
+++

Wie bereits in unserem [letzten Artikel](/unser-erstes-segeljahr) erwähnt, brechen wir im April ins Mittelmeer auf. Doch bevor es losgehen kann, möchten wir die Futura noch etwas besser ausstatten und ihr neuen Glanz verleihen ⛵

<!-- more -->

### Cockpit Holz

Das Holz im Cockpit sah an vielen Stellen schon ziemlich mitgenommen aus und immer mehr Fugen haben sich gelöst. Um zu verhindern, dass unser Cockpit bald wie ein Schweizer Käse aussieht, mussten wir hier unbedingt ran. 


{{ imgpair(
  url_left="/img/winterprojekte/PXL_20230113_101251077.MP.jpg",
  text_left="Die alten Fugen sind spröde, stehen raus und lösen sich ab."
  url_right="/img/winterprojekte/PXL_20230113_111145019.jpg",
  text_right="Mit Teppichmesser, Fugenhaken, Schraubenzieher und Dremel werden die alten Fugen entfernt"
)}}


Die [Anleitung von Simon](https://sailingbritican.com/teak-deck-repair) (auch als [Video](https://www.youtube.com/watch?v=kv7Ez2gdw0k)) hat uns hierbei sehr geholfen und es hat überwiegend auch gut funktioniert. 

{{ imgpair(
  url_left="/img/winterprojekte/PXL_20230113_144847061.jpg",
  text_left="Nach dem Abkleben werden die Fugen mit der Masse gefüllt"
  url_right="/img/winterprojekte/PXL_20230113_145419946.jpg",
  text_right="Anschließend glatt gestrichen und ca. 30 Minuten gewartet bevor das Band entfernt wird."
)}}

{{ imgpair(
  url_left="/img/winterprojekte/PXL_20230114_145755263.jpg",
  text_left="Bis zum Schleifen muss die Masse vier Tage aushärten"
  url_right="/img/winterprojekte/PXL_20230118_133151880.jpg",
  text_right="Nach dem Schleifen sind wir mit dem Ergebnis zufrieden"
)}}

Als Fugenmasse haben wir [Pantera Marine Deck](https://www.svb24.com/en/pantera-grouting-compound-md3000-30-v3.html) verwendet, welches wesentlich zäher beim Auftragen ist als die Fugenmasse von Sika Flex, was wir bei der Verarbeitung allerdings als Vorteil empfanden.

### Solar & Elektronik

Der größte Punkt auf unserer Liste der Winterprojekte war jedoch der Austausch unseres schwachen Solarpanels und die Teilüberholung der Bordelektronik. Die Elektronik an Bord ist unumgänglich auch ein wichtiger Aspekt der Sicherheit an Bord und so haben wir uns mit Peer professionelle Hilfe dazu geholt. Peer hatte uns bereits kurz nach dem Kauf der Futura mit Rat und Tat zur Seite gestanden und wir hatten jetzt das große Glück, dass er mit seiner SY Second Life gerade gar nicht weit entfernt von uns ebenfalls an der Algarve liegt.

Folgende Punkte brauchten unsere Aufmerksamkeit:

  - Unsere drei neuen Batterien mussten wieder auf zwei Stromkreise aufgeteilt werden nachdem diese zunächst provisorisch alle drei parallel geschaltet wurden
  - Die Verkabelung war nicht professionell und für uns auch nicht wirklich nachvollziehbar
  - Es gab keine Sicherungen unmittelbar an den Batterien
  - Viele Verbindungen waren bereits korrodiert oder schlimmer noch angeschmort
  - Das bestehende Solarpanel hat kaum mehr als 15 Watt Leistung geliefert.
  - Der bestehende Solarladeregler war nicht mehr state of the art und ineffizient


Als ersten Schritt haben wir uns daran gemacht alle Kabel, die von den Batterien und den Hauptschaltern abgehen zu identifizieren und zu beschriften. Anschließend wurden die Stromkreise wieder getrennt, sodass nur noch zwei der drei Batterien parallel geschaltet sind und eine Batterie exklusiv für den Motor bleibt. So eine Trennung ist wichtig und sicherheitsrelevant, damit man nicht versehentlich durch zu viele Verbraucher die Starterbatterie soweit leert, dass der Motor nicht mehr starten kann.

{{ imgpair(
  url_left="/img/winterprojekte/WhatsApp Image 2023-02-08 at 09.35.15.jpg",
  text_left="Alles hübsch sortiert und beschriftet"
  url_right="/img/winterprojekte/WhatsApp Image 2023-02-03 at 17.57.18.jpg",
  text_right="Verkabelung, Messshunt, Ladestromverteiler - alles sauber und ordentlich"
)}}

Beim Entwirren der Kabel zeigte sich auch, dass das Landladegerät ebenfalls ein Fall fürs Museum ist. Im ursprünglichen Zustand beim Kauf waren Land- und Solarladegerät auf eine Trenndiode geschaltet, die den Strom dann auf zwei Stromkreise aufgeteilt hat. Da eine herkömmliche Trenndiode jedoch einen Spannungsverlust verursacht war dies ineffizient und nicht mehr zeitgemäß. Wir haben ein neues [Victron Blue Smart Landladegerät](https://www.svb.de/de/victron-ladegeraet-bluesmart-ip-22-12-v-20-a-3-ladeausgaenge.html) verbaut, welches über mehrere getrennte Ausgänge unsere beiden Stromkreise jeweils direkt bedienen kann. Die Trenndiode haben wir durch einen [modernen Ladestromverteiler ohne Spannungsverlust](https://www.svb.de/de/mastervolt-ladestromverteiler-battery-mate-1602-ig-mosfet-160-a-2-batteriebaenke.html) ersetzt.

{{ subscribe()}}

Für unser neues Solarpanel haben wir ebenfalls von Victron einen [effizienten MPPT Laderegler](https://www.svb.de/de/victron-solar-laderegler-smartsolar-mppt-100-20.html) verbaut, der so geschaltet ist, dass er die Service Batterien lädt.

Und damit wir jederzeit genau sehen können wie viel Strom in das System gespeist oder verbraucht wird, haben wir noch einen [Victron Smart Shunt](https://www.svb.de/de/victron-smartshunt-inkl-bluetooth-500-a.html) verbaut. Alle drei Geräte von Victron verfügen über Bluetooth und können über eine einzige App überwacht werden was wirklich sehr gut funktioniert. Das ganze bringt zudem gegenüber einem einzelnen fest verbauten Monitor eine gewisse Redundanz, da wir die App sowohl auf unserem Navigations Tablet als auch zwei Handys betreiben können.

{{ imgpair(
  url_left="/img/winterprojekte/signal-2023-02-09-133906.jpg",
  text_left="Das Panel bei Vormittagssonne"
  url_right="/img/winterprojekte/signal-2023-02-09-133838.jpg",
  text_right="Drei Geräte in einer App, unser Smart Home."
)}}

Die Batterien wurden schließlich noch mit 200A Sicherungen abgesichert und alle Verbindungen mit ordentlichen Kabelschuhen und Isolierungen erneuert.

Obwohl hier natürlich schon ein paar Kosten entstanden sind, haben wir die Investitionen dennoch begrenzt, da wir planen in absehbarer Zeit noch einmal auf ein größeres Schiff umzusteigen. Deshalb haben wir uns auch gegen einen großen Geräteträger und ein massives Aufgebot an Solarpanelen entschieden sondern lediglich die bestehende Befestigungslösung für ein größeres Panel genutzt. Da uns hier also bereits bestehende Einschränkungen vorlagen galt es ein Panel zu finden, dass ca eine Größe von 1 x 1 Meter hat und dabei die größtmögliche Leistung liefert. Tatsächlich haben wir dann bei Leeroy Merlin ein [190 Watt Panel von Xunzel](https://www.leroymerlin.pt/produtos/eletricidade-e-smart-home/energias-renovaveis/paineis-solares/painel-solar-xunzel-power-190w-12v-c-cabo-83795761.html) gefunden, das unsere Vorgaben erfüllt hat. 

{{ imgpair(
  url_left="/img/winterprojekte/PXL_20230204_160119656.MP.jpg",
  text_left="Zur Stabilität wird der Alurahmen durch Holz verstärkt"
  url_right="/img/winterprojekte/PXL_20230205_094714208.jpg",
  text_right="Hier hängen 190 Watt mit einem Panel"
)}}

Wir haben den Alurahmen mit einem Holzrahmen unterfüttert, das ganze mit Epoxy bestrichen, silber lackiert und mit den bestehenden Halterungen an unserem geteilten Achterstag aufgehangen. Mit dem Ergebnis sind wir sehr zufrieden!

### Motor, Rigg & neuer Anker

Unser Dieselvorfilter sah so aus als wurde er seit Jahren nicht mehr gewechselt. Wir haben einen neuen montiert und die Gelegenheit genutzt und direkt noch einen Öl- und Ölfilterwechsel gemacht.

{{ imgpair(
  url_left="/img/winterprojekte/PXL_20230206_124614743.jpg",
  text_left="Ihr könnt euch vorstellen, wie das Teil von innen aussah!"
  url_right="/img/winterprojekte/PXL_20230206_124619193.jpg",
  text_right="Das neue Glanzstück im Motorraum."
)}}

Da Christoph zuletzt vor einem Jahr im Mast war und wir auch unsere neue Strickleiter ausprobieren wollten (Das nächste Boot bekommt Maststufen!) ging es auch noch einmal hoch hinaus. Wir haben die Gelegenheit genutzt um ein zusätzliches Fall anzubringen und direkt das Radar abmontiert, welches ohnehin bereits beim Kauf defekt war.

{{ imgpair(
  url_left="/img/winterprojekte/IMG-20230205-WA0003.jpg",
  text_left="Es ist immer aufregend in den Mast zu gehen aber die Aussicht ist traumhaft"
  url_right="/img/winterprojekte/PXL_20230205_120427656.jpg",
  text_right="Das alte Radar kommt runter"
)}}

Zu guter Letzt ging es noch unserem alten 16 kg Anker an den Kragen. Der neue Anker ist eine Kopie des bewährten Delta Ankers mit 20 kg und sollte uns ruhige Nächte sichern.

{{imgwide(text="Ein Prachtstück mit viel Haltekraft für ein 10 Meter Boot", url="/img/winterprojekte/PXL_20230207_162252322.MP.jpg")}}

An dieser Stelle möchten wir uns wieder einmal ganz herzlich bei Peer bedanken, der seine knappe Zeit mit uns geteilt hat um unser Boot für neue Abenteuer vorzubereiten. Dabei legen wir großen Wert darauf selbst zu lernen wie anstehende Arbeiten fachgerecht erledigt werden. Mit seiner humorvollen, geduldigen Art verrichtet Peer nicht einfach nur Arbeiten sondern erfüllt gleichzeitig die Aufgabe eines Mentors der seinen großen Erfahrungsschatz bereitwillig mit uns Grünschnabeln teilt. Dafür sagen wir nochmals: DANKE Peer 🙏

{{ airbnb_ad()}}

