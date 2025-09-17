#Lathund – Installera bibliotek i venv

## 1. Öppna rätt mapp i terminalen
Gå till projektmappen där din venv finns:
```powershell
cd C:\Users\laura\OneDrive\Desktop\code\python-programming-Laura-Lomakin
```

## 2. Aktivera venv
**PowerShell:**
```powershell
.\venv\Scripts\activate
```
> Om du får “execution policy”-fel, kör först:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

**Git Bash:**
```bash
source venv/Scripts/activate
```

När `(venv)` syns framför raden är miljön aktiv.

## 3. Installera paket
```bash
pip install numpy matplotlib
```

## 4. Kolla att installationen lyckades
```bash
pip list
```
Eller testa direkt:
```bash
python -c "import numpy, matplotlib; print('OK!')"
```

## 5. Använd i notebook
I din `.ipynb`-fil (med kernel = venv) kan du nu skriva:
```python
import numpy as np
import matplotlib.pyplot as plt
```

---

*Referens: ChatGPT (2025)*
