// Vid1
import Header from "./vid1/Header.jsx";
import Footer from "./vid1/Footer.jsx";
import Food from "./vid1/Food.jsx";

// vid2
import Card from './vd2/Card.jsx'

//vid3
import Button from "./vid3/Button.jsx";

function App() {

  return (
    <>
      <Header />

      <div>
        <Card />
        <Card />
        <Card />
        <Card />
      </div>
      
      <Button />

      <div>
        <Food />
        <Food />
        <Food />
        <Food />
        <Food />
      </div>

      <Footer />
    </>
  );
}

export default App
