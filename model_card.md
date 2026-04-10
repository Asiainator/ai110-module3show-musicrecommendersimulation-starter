# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **JuJu Song Radar*  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

It is a simple song recommender based on if a song is your favoruite genre, if it's your favoruite mood and how close the energy of the song is to your perfect song.

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Genre and Mood give a huge priorites and energy is equivalent to if the Genre and Mood were the same if it was perfectly suited to the person but Energy is a spectrum and genre and mood being binary yes or no additions.

score = (1.0 if genre matches else 0)
      + (1.0 if mood matches else 0)
      + 2.0 × (1.0 - |user_energy - song_energy|)


Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

"Starter (Pop/Happy)": {
        "genre": "pop", "mood": "happy", "energy": 0.8
    },
    "High-Energy Pop": {
        "genre": "pop", "mood": "happy", "energy": 0.95
    },
    "Chill Lofi": {
        "genre": "lofi", "mood": "chill", "energy": 0.35
    },
    "Deep Intense Rock": {
        "genre": "rock", "mood": "intense", "energy": 0.90
    },

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Energy levels near .50 because it has more to work with.

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Because of the Energy gap being Linear it gives low energy users worse recomedations but because of how linear works it will give more options and better options near .50 as that has the most options and .100 and .0 energy listeners are unfairly treated.

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Calculated myself and had easy to calculate numbers based on the Genre and Mood making simple, the weight shift suprised me the most as it had some weird affects on certain genres.

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Maybe make Genre and Mood more like an spectrum like a bell curve almost of Genre and Moods as certain genre and mood are close, making an adjanceny list or bell curve also would love to include more variables. 

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

I think i'm gettting more proficient at using AI as a tool and building this recommended has informed me about how simple recommendations can be and how easy this type of thing can expand.

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
