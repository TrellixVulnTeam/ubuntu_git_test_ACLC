��    �      �  �   l      0     1     3  "   ;  �  ^     �  (   �  #   '     K     a  &   w     �     �     �  *   �          -     5  9   <  )   v     �  "   �     �     �  /     +   6     b     u     ~     �  #   �  #   �  %   �           .     B     U     m     �     �  W   �       "   %     H  &   f  "   �     �     �     �     �       !   5     W  '   t  "   �     �     �  !   �  #        3  !   F  %   h     �     �  !   �     �  &   �  5   $  *   Z  C   �  =   �       (     %   B  %   h  0   �  &   �     �  /   �     (  >   :  @   y     �     �     �  3   �  ,   !     N     b     x     �     �     �  '   �     �  '        :     Q     g  +   v     �     �     �     �     	          .     A     R  	   b     l  %   �  /   �     �     �           !   &   @      g   !   �      �      �      �   1   �   /   !     2!  !   ?!     a!  ,   }!  T   �!     �!  
   "      �"     �"     �"     �"     �"     �"     �"     #  4   .#  $   c#     �#     �#     �#     �#     �#     $  *   3$  :   ^$     �$      �$  )   �$     %  #   %  #   C%  0   g%     �%     �%  
   �%     �%     �%     �%     �%     &     *&  %   B&     h&     �&     �&     �&  &   �&     �&     �&     '     &'     B'  4   S'     �'     �'     �'  �  �'     B)     D)  *   P)  �  {)  .   x-  .   �-  )   �-  "    .     #.  &   >.     e.     �.     �.  1   �.  "   �.  
   �.     /  S   /  5   a/     �/  4   �/     �/     �/  :   0  '   F0     n0     �0     �0     �0  ,   �0  ,   �0  (   1  )   G1     q1     �1     �1     �1     �1     �1  b   2      p2  +   �2  !   �2  -   �2  ,   3     :3     X3     s3     �3  '   �3  '   �3  &   �3  )   &4  *   P4     {4  "   �4  /   �4  (   �4     5  (   %5  (   N5  !   w5  %   �5  %   �5  -   �5  8   6  :   L6  ,   �6  E   �6  <   �6  
   77  0   B7  #   s7  #   �7  9   �7  9   �7      /8  ?   P8     �8  C   �8  E   �8     09     39     R9  B   n9  ,   �9     �9     �9     :     ,:     H:     a:  (   :     �:  2   �:     �:     ;     6;  .   J;  "   y;     �;     �;     �;     �;     �;     <     +<     C<     Y<     f<  %   }<  2   �<      �<  #   �<     =  $   )=     N=  %   k=  )   �=     �=     �=     �=  1   �=  /   >     I>     U>     n>  .   �>  h   �>  �   "?     �?  %   �?     �?     �?     @     )@     >@  &   X@  +   @  8   �@  "   �@  !   A  +   )A     UA     uA     �A     �A  '   �A  <   �A  %   -B  (   SB  9   |B  %   �B  %   �B  +   C  1   .C     `C     rC     �C     �C     �C     �C     �C     �C     �C     D     #D  #   :D  &   ^D     �D  .   �D     �D     �D     �D  !   E     $E  2   8E     kE     sE     uE         �          b   �       �   $          �       w   a       �          y      �   �   �           �   P   �   \   d   H   i   Z       t       `   �   F           z       �       |   �              5   �   �           x   '   h          4      e   �   {          �   �       L   �           *   "       @       n   N   K   �   �   �   =   l          �           Y   A          �   �   Q      >      &      ;   T      /   	   u       U   +   j   8   �       r   �          D          R   �       _   �   �   �       �   %   G   �   �   #   V       2       }   �   �      E   W   �   S   s      I   �          (   �   ?         [   �   ,   O      9   1       �   J       �   �   
   �       M   �   3       ]       �       )          �          �   -       q          g   k   �   :          o       �          6   B   �   <       �   f   ~       7          X   p       C       0   m   �              v   ^   .   �           !   c    
 
(None) 
Error applying application rules. 
Usage: %(progname)s %(command)s

%(commands)s:
 %(enable)-31s enables the firewall
 %(disable)-31s disables the firewall
 %(default)-31s set default policy
 %(logging)-31s set logging to %(level)s
 %(allow)-31s add allow %(rule)s
 %(deny)-31s add deny %(rule)s
 %(reject)-31s add reject %(rule)s
 %(limit)-31s add limit %(rule)s
 %(delete)-31s delete %(urule)s
 %(insert)-31s insert %(urule)s at %(number)s
 %(reload)-31s reload firewall
 %(reset)-31s reset firewall
 %(status)-31s show firewall status
 %(statusnum)-31s show firewall status as numbered list of %(rules)s
 %(statusverbose)-31s show verbose firewall status
 %(show)-31s show firewall report
 %(version)-31s display version information

%(appcommands)s:
 %(applist)-31s list application profiles
 %(appinfo)-31s show information on %(profile)s
 %(appupdate)-31s update %(profile)s
 %(appdefault)-31s set default application policy
  (skipped reloading firewall)  Attempted rules successfully unapplied.  Some rules could not be unapplied. %s is group writable! %s is world writable! '%(f)s' file '%(name)s' does not exist '%s' already exists. Aborting '%s' does not exist '%s' is not writable (be sure to update your rules accordingly) : Need at least python 2.6)
 Aborted Action Added user rules (see 'ufw status' for running firewall): Adding IPv6 rule failed: IPv6 not enabled Available applications: Backing up '%(old)s' to '%(new)s'
 Bad destination address Bad interface name Bad interface name: can't use interface aliases Bad interface name: reserved character: '!' Bad interface type Bad port Bad port '%s' Bad source address Cannot insert rule at position '%d' Cannot insert rule at position '%s' Cannot specify 'all' with '--add-new' Cannot specify insert and delete Checking ip6tables
 Checking iptables
 Checking raw ip6tables
 Checking raw iptables
 Checks disabled Command '%s' already exists Command may disrupt existing ssh connections. Proceed with operation (%(yes)s|%(no)s)?  Could not back out rule '%s' Could not delete non-existent rule Could not find '%s'. Aborting Could not find a profile matching '%s' Could not find executable for '%s' Could not find profile '%s' Could not find protocol Could not find rule '%d' Could not find rule '%s' Could not get listening status Could not get statistics for '%s' Could not load logging rules Could not normalize destination address Could not normalize source address Could not perform '%s' Could not set LOGLEVEL Could not update running firewall Couldn't determine iptables version Couldn't find '%s' Couldn't find parent pid for '%s' Couldn't find pid (is /proc mounted?) Couldn't open '%s' for reading Couldn't stat '%s' Couldn't update application rules Couldn't update rules file Couldn't update rules file for logging Default %(direction)s policy changed to '%(policy)s'
 Default application policy changed to '%s' Default: %(in)s (incoming), %(out)s (outgoing), %(routed)s (routed) Deleting:
 %(rule)s
Proceed with operation (%(yes)s|%(no)s)?  Description: %s

 Duplicate profile '%s', using last found ERROR: this script should not be SGID ERROR: this script should not be SUID Firewall is active and enabled on system startup Firewall not enabled (skipping reload) Firewall reloaded Firewall stopped and disabled on system startup Found exact match Found multiple matches for '%s'. Please use exact profile name Found non-action/non-logtype match (%(xa)s/%(ya)s %(xl)s/%(yl)s) From IPv6 support not enabled Improper rule syntax Improper rule syntax ('%s' specified with app rule) Insert position '%s' is not a valid position Invalid '%s' clause Invalid 'from' clause Invalid 'port' clause Invalid 'proto' clause Invalid 'to' clause Invalid IP version '%s' Invalid IPv6 address with protocol '%s' Invalid interface clause Invalid interface clause for route rule Invalid log level '%s' Invalid log type '%s' Invalid option Invalid policy '%(policy)s' for '%(chain)s' Invalid port with protocol '%s' Invalid ports in profile '%s' Invalid position ' Invalid position '%d' Invalid profile Invalid profile name Invalid token '%s' Logging disabled Logging enabled Logging:  Missing policy for '%s' Mixed IP versions for 'from' and 'to' Must specify 'tcp' or 'udp' with multiple ports Need 'from' or 'to' with '%s' Need 'to' or 'from' clause New profiles: No ports found in profile '%s' No rules found for application profile Option 'log' not allowed here Option 'log-all' not allowed here Port ranges must be numeric Port: Ports: Profile '%(fn)s' has empty required field '%(f)s' Profile '%(fn)s' missing required field '%(f)s' Profile: %s
 Profiles directory does not exist Protocol mismatch (from/to) Protocol mismatch with specified protocol %s Resetting all rules to installed defaults. Proceed with operation (%(yes)s|%(no)s)?  Resetting all rules to installed defaults. This may disrupt existing ssh connections. Proceed with operation (%(yes)s|%(no)s)?  Rule added Rule changed after normalization Rule deleted Rule inserted Rule updated Rules updated Rules updated (v6) Rules updated for profile '%s' Skipped reloading firewall Skipping '%(value)s': value too long for '%(field)s' Skipping '%s': also in /etc/services Skipping '%s': couldn't process Skipping '%s': couldn't stat Skipping '%s': field too long Skipping '%s': invalid name Skipping '%s': name too long Skipping '%s': too big Skipping '%s': too many files read already Skipping IPv6 application rule. Need at least iptables 1.4 Skipping adding existing rule Skipping inserting existing rule Skipping malformed tuple (bad length): %s Skipping malformed tuple: %s Skipping unsupported IPv4 '%s' rule Skipping unsupported IPv6 '%s' rule Status: active
%(log)s
%(pol)s
%(app)s%(status)s Status: active%s Status: inactive Title: %s
 To Unknown policy '%s' Unsupported action '%s' Unsupported default policy Unsupported direction '%s' Unsupported policy '%s' Unsupported policy for direction '%s' Unsupported protocol '%s' WARN: '%s' is world readable WARN: '%s' is world writable Wrong number of arguments You need to be root to run this script n problem running problem running sysctl problem running ufw-init
%s running ufw-init uid is %(uid)s but '%(path)s' is owned by %(st_uid)s unknown y yes Project-Id-Version: ufw
Report-Msgid-Bugs-To: FULL NAME <EMAIL@ADDRESS>
POT-Creation-Date: 2014-02-20 14:16-0600
PO-Revision-Date: 2012-11-25 20:06+0000
Last-Translator: Andrej Znidarsic <andrej.znidarsic@gmail.com>
Language-Team: Slovenian <sl@li.org>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
X-Launchpad-Export-Date: 2015-01-26 20:08+0000
X-Generator: Launchpad (build 17306)
 
 
(Ničesar) 
Napaka med uveljavljanjem pravil programa 
Uporaba: %(progname)s %(command)s

%(commands)s:
 %(enable)-31s omogoči požarni zid
 %(disable)-31s onemogoči požarni zid
 %(default)-31s nastavi privzeti pravilnik
 %(logging)-31s nastavi beleženje na %(level)s
 %(allow)-31s dodaj dovoli %(rule)s
 %(deny)-31s dodaj prepovej %(rule)s
 %(reject)-31s dodaj zavrni %(rule)s
 %(limit)-31s dodaj omejitev %(rule)s
 %(delete)-31s izbriši %(urule)s
 %(insert)-31s vstavi %(urule)s na %(number)s
 %(reload)-31s ponovno naloži požarni zid
 %(reset)-31s ponastavi požarni zid
 %(status)-31s prikaži stanje požarnega zidu
 %(statusnum)-31s prikaži stanje požarnega zidu kot oštevilčen seznam %(rules)s
 %(statusverbose)-31s prikaži podrobni izpis stanja požarnega zidu
 %(show)-31s prikaži poročilo požarnega zidu
 %(version)-31s prikaži podrobnosti različice
%(appcommands)s:
 %(applist)-31s navedi profile programov
 %(appinfo)-31s prikaži podatke %(profile)s
 %(appupdate)-31s posodobi %(profile)s
 %(appdefault)-31s nastavi privzet pravilnik programov
  (preskok ponovnega nalaganja požarnega zidu)  Poskušana pravila so uspešno oduveljavljena  Nekaterih pravil ni mogoče razveljaviti V %s lahko pišejo člani skupine! V %s lahko piše kdorkoli! '%(f)s' datoteka '%(name)s' ne obstaja '%s' že obstaja. Prekinitev '%s' ne obstaja '%s' ni zapisljivo (zagotovite ustrezno posodabljanje vaših pravil) : zahtevan je najmanj python 2.6)
 Preklicano Dejanje Dodana uporabniška pravila (za izvajanje požarnega zidu si oglejte 'ufw status'): Dodajanje pravil za IPv6 ni uspelo: IPv6 ni omogočen Dostopni programi: Ustvarjanje varnostne kopije '%(old)s' na '%(new)s'
 Neveljaven ciljni naslov Slabo ime vmesnika Slabo ime vmesnika: vzdevkov vmesnika ni mogoče uporabiti Slabo ime vmesnika: pridržan znak: '!' Slaba vrsta vmesnika Neveljavna vrata Neveljavna vrata '%s' Neveljaven izvorni naslov Pravila ni mogoče vstaviti na položaj '%d' Pravila ni mogoče vstaviti na položaj '%s' Z '--add-new' ni mogoče določiti 'all' Vstavitve in izbrisa ni mogoče določiti Preverjanje ip6tables
 Preverjanje iptables
 Preverjanje surovih ip6tables
 Preverjanje surovih iptables
 Preverjanje je onemogočeno Ukaz '%s' že obstaja Ukaz lahko prekine obstoječe povezave ssh. Ali želite nadaljevati z opravilom (%(yes)s|%(no)s)?  Pravila '%s' ni mogoče umakniti Neobstoječega pravila ni mogoče izbrisati Ni mogoče najti '%s'. Prekinitev Profila skladajočega z '%s' ni mogoče najti Izvršilne datoteke za '%s' ni mogoče najti Profila '%s' ni mogoče najti Protokola ni mogoče najti Ni mogoče najti pravila '%d' Ni mogoče najti pravila '%s' Ni mogoče pridobiti stanja poslušanja Ni mogoče pridobiti statistike za '%s' Pravil beleženja ni mogoče naložiti Ciljnega naslova ni mogoče normalizirati Izvornega naslova ni mogoče normalizirati '%s' ni mogoče izvesti RAVNIDNEVNIKA ni mogoče nastaviti Požarnega zidu ni mogoče posodobiti med tekom Ni mogoče določiti različice iptables '%s' ni mogoče najti Nadrejenega pid za '%s' ni mogoče najti Ni mogoče najti (je /proc priklopljen?) '%s' ni mogoče odpreti za branje Ukaza stat ni mogoče izvesti na '%s' Pravil programa ni mogoče posodobiti Datoteke s pravili ni bilo mogoče posodobiti Ni bilo mogoče posodobiti datoteke pravil za beleženje Privzeto pravilo %(direction)s spremenjeno v '%(policy)s'
 Privzeto pravilo programa spremenjeno v '%s' Privzeto: %(in)s (dohodni), %(out)s (odhodni), %(routed)s (usmerjeni) Brisanje:
 %(rule)s
Nadaljevanje opravila (%(yes)s|%(no)s)?  Opis: %s

 Dvojnik profila '%s', uporaba zadnjega najdenega NAPAKA: ta skripta ne sme biti SGID NAPAKA: ta skripta ne sme biti SUID Požarni zid je dejaven in omogočen ob sistemskem zagonu Požarni zid ni onemogočen (preskok ponovnega nalaganja) Požarni zid je ponovno naložen Požarni zid je zaustavljen in onemogočen ob sistemskem zagonu Najden točen zadetek Najdenih je bilo več ujemanj za '%s'. Uporabite točno ime profila Najden ne-dejavni/ne-dnevniški zadetek (%(xa)s/%(ya)s %(xl)s/%(yl)s) Od Poodpora za IPv6 ni omogočena Neveljavno pravilo skladnje Nepravilna skladnja pravila ('%s' je določen s pravilom programa) Vstavljen položaj '%s' ni veljaven položaj Neveljavna določba '%s' Neveljavna določba 'od' Neveljavna določba 'vrata' Neveljavna določba 'proto' Neveljavna določba 'do' Neveljavna različica IP '%s' Neveljaven naslov IPv6 s protokolom '%s' Neveljavna določba vmesnika Neveljavna določba vmesnika za pravilo usmerjanja Neveljavna raven dnevnika '%s' Neveljavna vrsta dnevnika '%s' neveljavna možnost Neveljavno pravilo '%(policy)s' za '%(chain)s' Neveljavna vrata s protokolom '%s' Neveljavna vrata v profilu '%s' Neveljaven položaj ' Neveljaven položaj '%d' Neveljaven profil Neveljavno ime profila Neveljaven žeton '%s' Beleženje onemogočeno Beleženje omogočeno Beleženje:  Manjka pravilo za '%s' Mešane različice IP za 'od' in 'do' Potrebno je določiti 'tcp' ali 'udp' z več vrati Z '%s' je zahtevan 'od' ali 'do' Zahtevana je določba 'od' ali 'za' Novi profili: V profilu '%s' ni mogoče najti vrat Ni pravil za profil programa Možnost 'beleži' tukaj ni dovoljena Možnost 'beleži-vse' tukaj ni dovoljena Obseg vrat mora biti število Vrata: Vrata: Profil '%(fn)s' ima prazno zahtevno polje '%(f)s' Profilu '%(fn)s' manjka zahtevano polje '%(f)s' Profil: %s
 Mapa profilov ne obstaja Neustrezen protokol (od/do) Neustrezen protokol z določenim protokolom %s Ponastavljanje vseh pravil na privzete vrednosti. Ali želite nadaljevati z opravilom (%(yes)s|%(no)s)?  Ponastavljanje vseh pravil na privzete vrednosti. Ukaz lahko prekine obstoječe povezave ssh. Ali želite nadaljevati z opravilom (%(yes)s|%(no)s)?  Pravilo dodano Pravilo je spremenjeno po izenačenju Pravilo izbrisano Pravilo je vstavljeno Pravilo posodobljeno Pravila posodobljena Pravila posodobljena (v6) Pravila za profil '%s' so posodobljena Preskok ponovnega nalaganja požarnega zidu Preskok '%(value)s': vrednost je predolga za '%(field)s' Preskok '%s': tudi v /etc/services Preskok '%s': ni mogoče obdelati Preskok '%s': ukaza stat ni mogoče izvesti Preskok '%s': polje je predolgo Preskok '%s': neveljavno ime Preskok '%s': ime je predolgo Preskok '%s': preveliko Preskok '%s': preveč prebranih datotek Preskok IPv6 pravila programa. Zahtevan je vsaj iptables 1.4 Preskok dodajanja obstoječega prvila Preskok vstavljanja obstoječega pravila Preskok slabo oblikovane n-terice (napačna dolžina): %s Preskok slabo oblikovane n-terice: %s Preskok nepodprtega pravila IPv4 '%s' Izpustitev nepodprtega pravila za IPv6 '%s' Stanje: dejavno
%(log)s
%(pol)s
%(app)s%(status)s Stanje: dejavno%s Stanje nedejavno Naslov: %s
 Za Neznano pravilo '%s' Nepodprto dejanje '%s' Nepodprta privzeta pravila Nepodprta smer '%s' Nepodprta pravila '%s' Nepodprta pravila za smer '%s' Nepodprt protokol '%s' OPOZORILO: '%s' lahko bere ves svet OPOZORILO: '%s' je splošno zapisljivo Napačno število argumentov Za zagon te skripte morate biti skrbnik (root) n težave z zagonom težave pri izvajanju sysctl napaka med izvajanjem ufw-init
%s zaganjanje ufw-init uid je %(uid)s toda '%(path)s ' nadzira %(st_uid)s neznano y da 