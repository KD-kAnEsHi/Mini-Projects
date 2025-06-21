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

//vid5
import UserGreeting from "./vid5-cond/userGreetings.jsx";

//vid6
import List from "./vid6-list/List.jsx"

//vi7
import Click from "./vid7-event/Click.jsx";
import ProfilePicture from "./vid7-event/profilePic.jsx";

//vid9
import MyComponent from "./vid9-onchange/MyComponents.jsx";


function App() {

  return (
    <>
      <Header />
      // vid-5
      <UserGreeting isLoggedIn={true} username="TheWallFacer"/>
      

      // vid-2
      <div>
        <Card />
        <Card />
        <Card />
        <Card />
      </div>


      // vid-3
      <Button />
      <Button />
      <Button />
      <Button />

      // vid4
      <Student name="Spongebob" age={13} isStudent={true} /> 
      <Student name="Patrick" age={23} isStudent={false} />
      <Student name="Logan" age={21} isStudent={true} />
      <Student name="Ryan" age={20} />
      <Student  isStudent={true} />
      <Student name="Aryan" age={20} isStudent={false} />

      // vid1
      <div>
        <Food />
        <Food />
        <Food />
        <Food />
        <Food />
      </div>

      // vid6
      <List/>

      //vid7
      <Click />
      <ProfilePicture />
      <ProfilePicture />

      // vid9
      <MyComponent />


      <Footer />
    </>

  );
}

export default App
