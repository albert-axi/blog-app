import { BrowserRouter as Router, Route } from 'react-router-dom'
import './App.css';
import UserPage from './components/UserPage';
import UserDetailsPage from './components/UserDetailsPage';

function App() {
  return (
    <div className="App">
      <Router>
        <Route exact path="/" render={() => <h1>Phase 4 Project</h1>} />
        <Route exact path="/users" component={UserPage} />
        <Route path="/users/:id" component={UserDetailsPage} />
      </Router>
    </div>
  );
}

export default App;
