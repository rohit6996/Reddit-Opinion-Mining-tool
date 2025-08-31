
# Reddit Opinion Polls

A Python project that fetches Reddit discussions on any question, analyzes user comments with NLP sentiment classification, and visualizes the overall opinion as a chart.

---

## 📌 Features

* 🔎 Search Reddit for **any question/topic** (searches across all of Reddit).
* 💬 Collects top comments from the most relevant post.
* 🧹 Preprocesses text (cleaning, stopwords removal).
* 🤖 Classifies comments into **Positive / Negative / Neutral** sentiment using VADER.
* 📊 Generates a **summary & visualization chart** of opinions.

---

## 🛠️ Tech Stack

* **Python 3.10+**
* [PRAW](https://praw.readthedocs.io/) – Reddit API Wrapper
* [NLTK](https://www.nltk.org/) – Natural Language Processing
* [Matplotlib](https://matplotlib.org/) – Data Visualization

---

## 📂 Project Structure

```
reddit-opinion-polls/
│── app/
│   ├── fetch_reddit.py       # Fetch posts & comments
│   ├── preprocessing.py      # Clean & preprocess text
│   ├── classifier.py         # Sentiment classification
│   ├── analyze_comments.py   # Apply NLP pipeline
│   ├── visualize_results.py  # Charts & visualization
│
│── main.py                   # Fixed question (old version)
│── main2.py                  # User input version (latest)
│── requirements.txt          # Dependencies
│── README.md                 # Project docs
```

---

## Testing

This project includes several testing modules to verify functionality:

- `main2.py` → Dummy testing file for quick experiments (not for production).
- `test_analyze_comments.py` → Tests comment analysis & sentiment classification.
- `test_fetch_comments.py` → Tests Reddit API comment fetching.
- `test_visualize_results.py` → Tests plotting and visualization output.

Run all tests with:
```bash
pytest



## ⚙️ Setup & Installation

1. **Clone repo**

   ```bash
   git clone https://github.com/your-username/reddit-opinion-polls.git
   cd reddit-opinion-polls
   ```

2. **Create virtual environment** (recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Reddit API credentials**

   * Create an app at [Reddit Apps](https://www.reddit.com/prefs/apps).
   * Add your `client_id`, `client_secret`, `user_agent` in `fetch_reddit.py`.

   Example:

   ```python
   reddit = praw.Reddit(
       client_id="YOUR_CLIENT_ID",
       client_secret="YOUR_CLIENT_SECRET",
       user_agent="RedditOpinionPolls/0.1"
   )
   ```

---

## 🚀 Usage

Run the user-input version:

```bash
python main2.py
```

Example:

```
Enter your Reddit poll question: Is junk food healthy?
```

✅ Output:

* Fetches most relevant Reddit discussion.
* Analyzes sentiment of comments.
* Plots a chart like this:

![Sample Chart](https://via.placeholder.com/600x300.png?text=Sentiment+Chart)

---

## 📊 Example Result

For the question **“Is AI dangerous?”**

| Sentiment | Count |
| --------- | ----- |
| Agree     | 15    |
| Disagree  | 12    |
| Neutral   | 5     |
| Offtopic  | 20    |

## Example Output

Here’s a sample visualization:

![Poll Results]("Mining result.png")


## 💡 Future Improvements

* Add topic modeling for deeper insights.
* Support multiple posts instead of one.
* Deploy as a web app with Flask/Streamlit.

---

## 📝 License

MIT License – feel free to use & improve!


