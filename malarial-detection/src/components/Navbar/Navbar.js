import 'bootstrap/dist/css/bootstrap.css';

import React, {useState} from 'react';
import {
  Collapse,
  Nav,
  Navbar,
  NavbarBrand,
  NavbarToggler,
  NavItem,
  NavLink,
} from 'reactstrap';

const HeaderNavbar =
    () => {
      const [isOpen, setIsOpen] = useState(false);

      const toggle = () => setIsOpen(!isOpen);

      return (
          <div><Navbar color = "light" light expand = "md">
          <NavbarBrand href = "/">Malaria
              Detection</NavbarBrand>
        <NavbarToggler onClick={toggle} />
          <Collapse isOpen = {isOpen} navbar><Nav className = "ml-auto" navbar>
          <NavItem><NavLink href = "/">Home</NavLink>
            </NavItem>
          <NavItem>
          <NavLink href = "/about">About</NavLink>
            </NavItem>
          <NavItem><NavLink href = "/demo">Demo</NavLink>
            </NavItem>
          </Nav>
        </Collapse></Navbar>
    </div>);
    }

export default HeaderNavbar;
