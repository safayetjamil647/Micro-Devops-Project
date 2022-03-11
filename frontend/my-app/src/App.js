import './App.css';
import { Link } from "react-router-dom";
function App() {
  return (
    <div className="App">
          <h1>Demo Service</h1>
          <nav
        style={{
          borderBottom: "solid 1px",
          paddingBottom: "1rem",
        }}
      >
        <Link to="/service-one">Service One</Link> |{" "}
        <Link to="/service-two">Service Two</Link>
      </nav>
    </div>
  );
}

export default App;
