import React from "react";
import styled from "styled-components";

const FooterContainer = styled.div`
  background: #212529;
  right: 0;
  left: 0;
  bottom: 0;
  color: white;
  display: flex;
  justify-content: center;
  padding: 24px;
  font-size: 17px;
`;

function Footer() {
  return <FooterContainer>감사합니다.</FooterContainer>;
}

export default Footer;
