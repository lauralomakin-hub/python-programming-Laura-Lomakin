## Labb 2 – Klassificering av Pichu och Pikachu
# slutar här fredag kl. 22.45:
Tror att grunduppgiften är klar. Jag är osäker på vad jag gjort på slutet. Behöver läsa lite. Men jag tror det funkar.
**Syfte:**  
Använd verktygen du lärt dig i Python för att implementera en förenklad maskininlärningsalgoritm.  

I den här laborationen finns (simulerad) data på Pichus och Pikachus längder och bredder. Du ska skapa en algoritm som, baserat på den givna datan, kan avgöra om en ny datapunkt ska klassificeras som **Pichu** eller **Pikachu**.

---

## Grunduppgift
Följ flödesschemat för att bygga den grundläggande algoritmen.

Exempeldata att testa på:  
- (25, 32) → Pikachu  
- (24.2, 31.5) → Pikachu  
- (22, 34) → Pikachu  
- (20.5, 34) → Pichu  

---

## Uppgifter
1. **Användarinmatning:**  
   - Låt användaren mata in en testpunkt.  
   - Låt algoritmen avgöra dess klass.  
   - Ta med felhantering för negativa tal och icke-numeriska inputs.  
   - Skriv ut användarvänliga felmeddelanden.

2. **Majoritetsröstning:**  
   - Den första approachen (närmsta punkten) kan klassificera fel om punkterna går in i varandra.  
   - Ändra algoritmen så att den istället väljer de **10 närmaste punkterna** till testpunkten.  
   - Klassificeringen avgörs av **majoritetsröstning**.

---

## Bonusuppgifter (frivilliga)
3. **Dela data i träning/test:**  
   - 100 punkter = träningsdata (50 Pikachu, 50 Pichu).  
   - 50 punkter = testdata (25 Pikachu, 25 Pichu).  

4. **Beräkna noggrannhet (accuracy):**  
   \[
   accuracy = \frac{TP + TN}{total}
   \]  
   - TP = True Positive (korrekt Pikachu)  
   - TN = True Negative (korrekt Pichu)  
   - FP = False Positive  
   - FN = False Negative  
   - Här räknas Pikachu som **positiv** och Pichu som **negativ**.  
   - För varje testpunkt: beräkna distansen till träningspunkterna.

5. **Upprepa experimentet:**  
   - Kör uppgift 3 och 4 tio gånger.  
   - Plotta en graf över accuracy.  
   - Rapportera medelaccuracy.

---

## Bedömning
**Godkänt:**  
- Grunduppgiften + uppgifter lösta på korrekt sätt.  
- Koden är kommenterad med relevanta kommentarer.  
- Bra val av variabelnamn.  
- Flera relevanta git commits.  

**Väl godkänt:**  
- Koden är enkel att följa och effektiv.  
- Välstrukturerad med lämpliga funktioner.  
- Kommentarerna är datavetenskapligt korrekta.  
- Samtliga uppgifter lösta.
