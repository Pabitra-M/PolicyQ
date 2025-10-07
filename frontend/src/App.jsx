import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./page/HomePage/Home";
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/logo" element={<logo />} /> 

      </Routes>
    </BrowserRouter>
  );
}

export default App;
