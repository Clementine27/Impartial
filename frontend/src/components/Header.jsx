import React from "react";
import { useNavigate } from 'react-router-dom';
import "./Header.css" 

export default function Header(){
    return (
    <>
        <div className="CustomHeader">
            <div className="NameHolder">
                <ButtonRedirecter route = "/" buttonName = "Impartial" header = "yea" />
            </div>

            <div className="NavigationHolder">
                <NavigationBar/>
            </div>

            <div className="CountryHolder">
                <ButtonRedirecter route = "/countries" buttonName = "Countries"/>

            </div>
            <div className="EventHolder">
                <ButtonRedirecter route = "/events" buttonName = "Events"/>
            </div>
            </div>
        <div className="horiLine"></div>
    </>
    

 )
}

function ButtonRedirecter({route, buttonName, header}){
    const navigate = useNavigate(); 
    return (
    <button className= {header ? "Button Header": "Button Regular"} 
            onClick={() => navigate(route)} >
        {buttonName}
     </button>); 
}


function NavigationBar(){
    return (
        <>    
            <form className="d-flex NavBar" role="search">
            <input className="form-control rounded-pill" type="search" placeholder="Search" aria-label="Search"/>
            </form>
        </>
    )
}
