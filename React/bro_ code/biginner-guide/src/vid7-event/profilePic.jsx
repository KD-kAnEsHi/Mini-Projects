

function ProfilePicture () {
    const imageurl = "./src/assets/profile.png";
    const handleClick = (e) => e.target.style.display = "none"
   
    return (
        <img onClick={(e) => handleClick(e)} src={imageurl}></img>
    )
}
export default ProfilePicture