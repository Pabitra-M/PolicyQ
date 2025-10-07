import React from "react";
import { useRef } from "react";
import { FaBars, FaTimes } from "react-icons/fa";
import "../navbar/navbar.css";

function Navbar() {
  const navRef = useRef();

  const showNavbar = () => {
    navRef.current.classList.toggle("responsive_nav");
  };
  return (
    <>
      <header>
        <h3> Logo </h3>
        <nav ref={navRef}>
          <a href="/#">Home</a>
          <a href="/#">Documantation</a>
          <a href="/#">Contact</a>
          <a href="/#">About us</a>
          <button className="nav-btn nav-close-btn" onClick={showNavbar}>
            <FaTimes />
          </button>
        </nav>
        <div>
        <div className="profile-sec">
          <img
            src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fstock.adobe.com%2Fimages%2Fuser-icon-symbol-of-business-people-or-avatar-profile-with-trendy-flat-style-icon-for-web-site-design-logo-app-ui-isolated-on-white-background-vector-illustration-eps-10%2F289492257&psig=AOvVaw017dIJgJdmK4RQ3Z-1CGyF&ust=1759912711153000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCOCvyfLXkZADFQAAAAAdAAAAABAE"
            alt=""
          />
        </div>
        <button className="nav-btn" onClick={showNavbar}>
          <FaBars />
        </button>
        </div>
      </header>
    </>
  );
}

export default Navbar;
