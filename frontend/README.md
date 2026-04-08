# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
AI Incident Assistant

AI Incident Assistant is an intelligent tool designed to automate IT incident management. It classifies tickets, predicts priority, assigns teams, provides AI-generated troubleshooting steps, and can even estimate business impact. It’s built with Flask for the backend and React for the frontend.

Features
📝 Ticket Analysis: Automatically categorizes incidents and detects priority.
⚡ Assigned Team Recommendation: Suggests the right IT team for each incident.
🤖 AI Solution Generation: Provides step-by-step troubleshooting instructions.
📊 Incident Impact Prediction: Estimates affected employees, downtime, and business risk.
🔍 Similar Past Incidents: Shows related tickets to assist troubleshooting.
🎤 Voice Incident Reporting: Users can speak incidents directly.
🌙 Dark Theme Frontend: Modern and user-friendly UI.
⚠ Recurring Issue Detection: Highlights issues that occur frequently.
Technologies Used
Backend: Python, Flask, REST API
Frontend: React, JavaScript, CSS (Dark Theme)
AI & ML: GPT-5 mini (via Gemini API) for solution generation
Other Services: RAG for knowledge base retrieval, priority detection, and team assignment
Installation
1. Clone the repository
git clone https://github.com/<your-username>/ai-incident-assistant.git
cd ai-incident-assistant
2. Setup Backend
# Create and activate Python virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
3. Setup Frontend
cd frontend
npm install
4. Running the Project

Start the Backend (Flask)

cd ../backend
python app.py

Start the Frontend (React)

cd ../frontend
npm start

Open http://localhost:3000
 in your browser.

Testing Accuracy

You can test system accuracy by running:

python test_accuracy.py

It will display:

Category Accuracy
Priority Accuracy
Assigned Team Accuracy
Project Structure
ai-incident-assistant/
│
├─ backend/          # Flask backend
│  ├─ services/      # ML & AI services
│  ├─ routes/        # Flask routes
│  └─ app.py         # Main Flask application
│
├─ frontend/         # React frontend
│  ├─ public/        # Static files
│  └─ src/           # React source code
│
├─ knowledge/        # Incident knowledge base
│  └─ incidents.json
│
└─ README.md