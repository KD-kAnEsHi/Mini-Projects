// Vid1
import Header from "./vid1-comp/Header.jsx";
import Footer from "./vid1-comp/Footer.jsx";
import Food from "./vid1-comp/Food.jsx";

// vid2
import Card from './vid2/Card.jsx'

//vid3
import Button from "./vid3-modules/Button.jsx";

//vid4
import Student from "./vid4-props/Student.jsx";

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
      <Button />
      <Button />
      <Button />

      // props
      <Student name="Spongebob" age={13} isStudent={true} /> 
      <Student name="Patrick" age={23} isStudent={false} />
      <Student name="Logan" age={21} isStudent={true} />
      <Student name="Ryan" age={20} />
      <Student  isStudent={true} />
      <Student name="Aryan" age={20} isStudent={false} />


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
