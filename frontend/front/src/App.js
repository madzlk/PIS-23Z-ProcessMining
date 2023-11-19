import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

const api_url = process.env.REACT_APP_API_URL;

function App() {
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`${api_url}/users`);
        const data = await response.json();
        console.log('API Response:', data);
        setUserData(data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []); // Empty dependency array ensures the effect runs only once on mount

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          API_URL: {api_url}
        </p>
        {userData && (
          <div>
            <h2>User Data:</h2>
            <pre>{JSON.stringify(userData, null, 2)}</pre>
          </div>
        )}
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
