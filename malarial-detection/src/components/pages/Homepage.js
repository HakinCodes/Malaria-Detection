import "../../assets/css/Homepage.css"

import React from "react";
import Image from "react-bootstrap/Image"

import logo from '../../assets/images/bg1.png';
import logo2 from '../../assets/images/bg2.png';

function Homepage() {
  return (
    // home page
    <div className="home">
    
      {/* home page part1 */}
      <div className="d-flex part1 col-md-12">
        <div style={{
    textAlign: 'right'}}>
          <Image src={logo} alt="Logo" className="bgimage1"/>  
        </div>
        <div className="side1 col-md-6 float-left">
          <div className="malaria">
            Malaria
          </div>
          <div className="sidetext">
            According to WHO the
  estimate number of malaria
  deaths stood at 405,
      000 in 2018 <
          /div>
          <a className="gradient-button gradient-button-1" href="#">Get Started</a >
          <br /></div> 
      </div>

          {/* home page part2 */}<div className = "d-flex part2 col-md-12">
          <div style = {{ textAlign: 'left' }}>
          <Image src = {logo2} alt = "Logo2" className = "bgimage2" />
          </div>
        <div className="side2 col-md-6 float-right ml-auto">
          <div className="sidetext">
            <div className="text1">
              Malaria is an acute febrills illness.
            </div>
          <div className = "text2">To detect and identify<strong>Malarial Cell<
              /strong> this tool provides 95% accuracy and help different communities 
            </div>
          </div>
          <a className="gradient-button gradient-button-1 btn2" href="#">Launch Detector</a>
          <br /></div> 
      </div>< /div>
  );
};

export default Homepage;
