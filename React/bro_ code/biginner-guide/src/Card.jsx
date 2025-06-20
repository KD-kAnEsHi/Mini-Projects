import profilepic from './assets/profile.png'

function Card() {
    return (
        <div className="card">
            <img className="card-image" src={profilepic} alt="profile picture"></img>
            <h2 className="card-title" >TheWallFacer</h2>
            <p className="card-text" >learning react, Building a startup</p>
        </div>
    );
}
export default Card