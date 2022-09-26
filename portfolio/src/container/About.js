import React, { useState, useEffect } from "react";
import styled, { css } from "styled-components";

import { Container, Row, Col } from "react-bootstrap";
import { FaBirthdayCake } from "react-icons/fa";
import { SiGithub } from "react-icons/si";
import { MdMail, MdCall } from "react-icons/md";
import { FaUniversity } from "react-icons/fa";
import image from "../assets/myphoto.jpeg";
import companyImg from "../assets/company.png";
import blogImg from "../assets/blog.png";

import { useMediaQuery } from "react-responsive";

function About() {
  const isPc = useMediaQuery({
    query: "(min-width:768px)",
  });
  const isMobile = useMediaQuery({
    query: "(max-width:767px)",
  });

  const [mode, setMode] = useState("");

  useEffect(() => {
    if (isPc) setMode("isPc");
    else if (isMobile) setMode("isMobile");
  }, [isMobile, isPc]);

  return (
    <CustomContainer id="About">
      <Row className="mt-5 title">
        <Col>
          <Title data-aos="fade-right" mode={mode}>
            프로필
          </Title>
        </Col>
      </Row>

      <Row className="content mt-5">
        <PhotoContainer className="col">
          <Portrait src={image} mode={mode} />
        </PhotoContainer>

        <Col>
          <h2 style={{ fontWeight: "bold" }}>박견우</h2>
          <h4>NEXT x Likelion 10기</h4>

          <ContentContainer>
            <li className="Birth" style={{ display: "flex" }}>
              <IconContainer>
                <FaBirthdayCake size="30" />
              </IconContainer>
              <div style={{ marginLeft: "24px" }}>
                <h5 style={{ margin: "0" }}>Birthday :</h5>
                <p style={{ margin: "0", fontSize: "17px" }}>1999.07.10</p>
              </div>
            </li>
          </ContentContainer>

          <ContentContainer>
            <li className="Phone" style={{ display: "flex" }}>
              <IconContainer>
                <MdCall size="30" />
              </IconContainer>
              <div style={{ marginLeft: "24px" }}>
                <h5 style={{ margin: "0" }}>Phone :</h5>
                <p style={{ margin: "0", fontSize: "17px" }}>
                  +82 10-2783-7229
                </p>
              </div>
            </li>
          </ContentContainer>

          <ContentContainer>
            <li className="University" style={{ display: "flex" }}>
              <IconContainer>
                <FaUniversity size="30" />
              </IconContainer>
              <div style={{ marginLeft: "24px" }}>
                <h5 style={{ margin: "0" }}>University / Department :</h5>
                <Anchor
                  style={{ margin: "0", fontSize: "17px" }}
                  href="https://www.korea.ac.kr/mbshome/mbs/university/index.do"
                  target="__blank"
                >
                  고려대학교
                </Anchor>
                <p style={{ display: "inline", fontSize: "17px" }}> / </p>
                <Anchor
                  style={{ margin: "0", fontSize: "17px" }}
                  href="https://hes.korea.ac.kr/hes/index.do"
                  target="__blank"
                >
                  보건환경융합과학부
                </Anchor>
              </div>
            </li>
          </ContentContainer>

          <ContentContainer>
            <li className="Company" style={{ display: "flex" }}>
              <IconContainer>
                <img
                  style={{ width: "30px" }}
                  src={companyImg}
                  alt="company png"
                />
              </IconContainer>
              <div style={{ marginLeft: "24px" }}>
                <h5 style={{ margin: "0" }}>Youtube :</h5>
                <Anchor
                  style={{ margin: "0", fontSize: "17px" }}
                  target="__blank"
                  href="https://www.youtube.com/wootakato"
                >
                  @wootakato
                </Anchor>
              </div>
            </li>
          </ContentContainer>

          <ContentContainer>
            <li className="EMail" style={{ display: "flex" }}>
              <IconContainer>
                <MdMail size="30" />
              </IconContainer>
              <div style={{ marginLeft: "24px" }}>
                <h5 style={{ margin: "0" }}>EMail :</h5>
                <Anchor
                  href="mailto:qkrrusdn747@korea.ac.kr"
                  style={{ margin: "0", fontSize: "17px" }}
                >
                  qkrrusdn747@korea.ac.kr
                </Anchor>
              </div>
            </li>
          </ContentContainer>

          <ContentContainer>
            <li className="GitHub" style={{ display: "flex" }}>
              <IconContainer>
                <SiGithub size="30" />
              </IconContainer>
              <div style={{ marginLeft: "24px" }}>
                <h5 style={{ margin: "0" }}>GitHub :</h5>
                <Anchor
                  style={{ margin: "0", fontSize: "17px" }}
                  href="https://github.com/Park747"
                  target="__blank"
                >
                  https://github.com/Park747
                </Anchor>
              </div>
            </li>
          </ContentContainer>

        </Col>
      </Row>
      <Row className="mt-5 mb-5">
        <Col style={{ textAlign: "center" }}>
          <br></br>
          <h4 style={{ fontWeight: "bold", marginBottom: "1rem" }}>
            코딩 6개월 차 평범한 대학생
          </h4>
          <IntroduceText>
            아이디어를 실현하는 것에 매력을 느껴<br></br>
            멋쟁이사자처럼 학회의 일원이 되었고
            현재는 제 손으로 개발공부를 하고 있습니다.
            <br />
            대단한 기술을 가지고 있는 건 아니지만
            프로젝트를 할 때마다 큰 보람을 느낍니다.
            <br />
          </IntroduceText>
        </Col>
      </Row>
    </CustomContainer>
  );
}

const CustomContainer = styled(Container)`
  padding-top: 90px;
  margin-top: 30px;
  padding-bottom: 70px;
`;

const Title = styled.h1`
  font-size: 45px;
  ${(props) =>
    props.mode === "isPc"
      ? css``
      : css`
          text-align: center;
        `}
`;

const Portrait = styled.img`
  object-fit: cover;
  border-radius: 50%;
  ${(props) =>
    props.mode === "isPc"
      ? css`
          width: 500px;
        `
      : css`
          width: 350px;
        `};
`;

const ContentContainer = styled.ul`
  list-style: none;
  padding: 0;
  margin-top: 20px;
`;

const IconContainer = styled.span`
  display: flex;
  justify-content: center;
  align-items: center;
`;

const PhotoContainer = styled.div`
  text-align: center;
  align-self: center;
`;

const IntroduceText = styled.p`
  text-align: center;
  font-size: 20px;
`;

const A = styled.h1`
  font-weight: bold;
  color: red;
  display: inline;
  font-size: 45px;
  text-decoration: underline;
  text-decoration-color: red;
`;

const Anchor = styled.a`
  margin: 0;
  font-size: 17px;
  color: black;

  &:hover {
    color: black;
  }
`;

export default About;
