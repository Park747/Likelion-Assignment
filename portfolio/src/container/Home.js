import React, { useState, useEffect } from "react";
import styled, { css } from "styled-components";
import jumbImg from "../assets/backimg.JPG";
import { useMediaQuery } from "react-responsive";

function Home() {
  let [mode, setMode] = useState("");
  let [quotesCnt, setQuotesCnt] = useState(0);
  const quotes = [
    `까칠하지만 속은 깊은`,
    "코딩을 잘하고 싶어하는",
    "도전적이고 싶지만 겁이 많은",
    "피아노와 패션을 사랑하는",
    `만족스런 삶을 위해 꾸준히 노력하는`,
  ];

  const mobileQuotes = [
    `까칠하지만 속은 깊은`,
    "코딩을 잘하고 싶어하는",
    "도전적이고 싶지만 겁이 많은",
    "피아노와 패션을 사랑하는",
    `만족스런 삶을 위해 꾸준히 노력하는`,
  ];
  const isPc = useMediaQuery({
    query: "(min-width:768px)",
  });
  const isMobile = useMediaQuery({
    query: "(max-width:767px)",
  });

  useEffect(() => {
    if (isPc) setMode("isPc");
    else if (isMobile) setMode("isMobile");
  }, [isMobile, isPc]);

  useEffect(() => {
    const interval = setInterval(() => {
      setQuotesCnt((c) => (c + 1) % quotes.length);
    }, 3000);
    return () => {
      clearInterval(interval);
    };
  }, [quotes.length]);

  return (
    <>
      <JumbotronContainer id="Home">
        <Image>
          <Contents pos={"leftTop"} mode={mode}>
            제 소개를 간단히 해보자면
          </Contents>
          {mode === "isPc"
            ? quotes.map((quote, index) => (
                <Quotes
                  stat={index === quotesCnt ? "active" : "hide"}
                  mode={mode}
                >
                  '{quote}'
                </Quotes>
              ))
            : mobileQuotes.map((quote, index) => (
                <Quotes
                  stat={index === quotesCnt ? "active" : "hide"}
                  mode={mode}
                >
                  '{quote}'
                </Quotes>
              ))}
          <Contents pos={"rightBot"} mode={mode}>
            사람입니다.
          </Contents>
        </Image>
      </JumbotronContainer>
    </>
  );
}

const JumbotronContainer = styled.div`
  position: relative;
  z-index: auto;
`;

const Image = styled.div`
  width: 100%;
  height: 100vh;

  display: flex;
  justify-content: space-between;
  flex-direction: column;

  background-attachment: fixed;
  background-image: url(${jumbImg});
  background-repeat: no-repeat;
  background-size: cover;
`;

const Contents = styled.h1`
  font-size: ${(props) => (props.mode === "isPc" ? "48px" : "36px")};
  color: white;
  text-align: ${(props) => (props.pos === "rightBot" ? "right" : "")};
  ${(props) =>
    props.mode === "isPc" && props.pos === "leftTop"
      ? css`
          margin-top: 200px;
          margin-left : 460px;
        `
      : null};
  ${(props) =>
    props.mode === "isPc" && props.pos === "rightBot"
      ? css`
          margin: 0 570px 150px 0; 
        `
      : null};

  ${(props) =>
    props.mode === "isMobile" && props.pos === "leftTop"
      ? css`
          margin: 165px 0 0 2rem;
        `
      : null};
  ${(props) =>
    props.mode === "isMobile" && props.pos === "rightBot"
      ? css`
          margin: 0 2rem 110px 0;
        `
      : null};

  display: inline-flex;
  justify-content: ${(props) => (props.pos === "rightBot" ? "end" : "")};
`;

const Quotes = styled.h1`
  font-size: ${(props) => (props.mode === "isPc" ? "40px" : "28px")};
  white-space: pre-line;
  text-align: center;
  color: white;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
  margin: 0;

  margin-top: 25px;

  transition: opacity 0.5s ease-out;

  ${(props) =>
    props.stat === "active"
      ? css`
          display: inline-block;
          opacity: 1;
        `
      : css`
          opacity: 0;
        `}
`;

export default Home;
