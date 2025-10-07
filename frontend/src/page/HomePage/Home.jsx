import Navbar from "../../components/navbar/Navbar"
import "../HomePage/home.css"

function Home() {
return (
    <div className="home-container">
      <div className="navbar">
        <Navbar />
      </div>
      <div className="content">
        <h1>Welcome to Home Page</h1>
        <p>Your content goes here...</p>
      </div>
    </div>
  );
}

export default Home
