Hapa ni mfumo kamili wa code kwa **Temp-Mail Python API Wrapper**, na jinsi ya kutumia API ya temp-mail.org kwa Python. Nitakupa mifano ya matumizi pamoja na maelezo muhimu ya kila hatua.

### 1. **Kusakinisha Library**

Ili kuanza, unahitaji kusakinisha library ya `temp-mail` kama ilivyoelezwa hapo awali. Ikiwa bado hujasakinisha, tumia:

```bash
pip install temp-mail
```

---

### 2. **Mfumo wa Code wa Temp-Mail API Wrapper**

Hapa chini ni mfano wa script ya Python ambayo inatumia **Temp-Mail Python API Wrapper**:

#### a) **Kupata Barua Pepe kutoka kwa Login na Domain Maalum**

Hii ni njia ya kupata barua pepe zote zinazotumwa kwa anwani maalum (login + domain).

```python
from tempmail import TempMail

# Initialize TempMail kwa login na domain maalum
tm = TempMail(login='ezra', domain='@gnail.pw')

# Kupata orodha ya barua pepe zinazotumwa kwa 'ezra@gnail.pw'
print("Emails zilizopatikana:")
emails = tm.get_mailbox()  
for email in emails:
    print(email)
```

**Maelezo:**  
- Hapa, tunatumia `login='ezra'` na `domain='@gnail.pw'` kuunda anwani ya barua pepe `ezra@gnail.pw`.
- `tm.get_mailbox()` itarudisha orodha ya barua pepe zote zilizotumwa kwa anwani hiyo.

---

#### b) **Kutengeneza Barua Pepe Mpya na Kupata Barua Pepe Zake**

Hii ni njia ya kutengeneza barua pepe mpya ya muda na kisha kupata barua pepe zote zinazotumwa kwa hiyo.

```python
from tempmail import TempMail

# Initialize TempMail bila login maalum (inajenga barua pepe random)
tm = TempMail()

# Kutengeneza anwani mpya ya barua pepe
email = tm.get_email_address()  
print(f"Barua Pepe Iliyotengenezwa: {email}")

# Kupata orodha ya barua pepe zinazotumwa kwa anwani hii
emails = tm.get_mailbox(email)
print("Emails zilizopatikana kwa barua pepe hii:")
for email in emails:
    print(email)
```

**Maelezo:**  
- `tm.get_email_address()` itarudisha anwani mpya ya barua pepe ya muda (mfano: `v5gwnrnk7f@gnail.pw`).
- Kisha, `tm.get_mailbox(email)` itakuonyesha barua pepe zilizotumwa kwa anwani hiyo.

---

### 3. **Mfano wa Matokeo**

#### a) **Output ya Kupata Barua Pepe kwa Login na Domain**

```plaintext
Emails zilizopatikana:
- Barua Pepe 1: "Test email 1"
- Barua Pepe 2: "Test email 2"
- Barua Pepe 3: "Test email 3"
```

#### b) **Output ya Kutengeneza Barua Pepe Mpya na Kupata Barua Pepe**

```plaintext
Barua Pepe Iliyotengenezwa: v5gwnrnk7f@gnail.pw
Emails zilizopatikana kwa barua pepe hii:
- Barua Pepe 1: "Verification email"
- Barua Pepe 2: "Newsletter"
```

---

### 4. **Kufanya Code Kuwa Haraka (Optional)**

Kama unahitaji kuboresha kasi ya code yako, unaweza kutumia `simplejson` badala ya `json` kwa ufanisi zaidi, haswa ikiwa unapata barua pepe nyingi au unafanya maombi ya API mara kwa mara.

#### a) **Install SimpleJSON**

```bash
pip install simplejson
```

#### b) **Update Code ili Kutumia SimpleJSON**

```python
import simplejson as json  # Badala ya 'import json'
```

Hii itasaidia kuongeza kasi ya usindikaji wa JSON.

---

### 5. **Hitimisho**

Hii ni mifano ya msingi ya kutumia **Temp-Mail Python API Wrapper**. Ukiwa na library hii, unaweza kutengeneza anwani za barua pepe za muda kwa urahisi, kuzipokea, na kuzipitisha kwa programu yako ya Python. Hii ni nzuri kwa kupunguza hatari ya kupata barua taka, majaribio ya huduma za barua pepe, na kulinda faragha yako.

---

Ikiwa unahitaji kubinafsisha au kuongeza vipengele vingine kwenye script yako, naweza kusaidia! Let me know! 🚀
