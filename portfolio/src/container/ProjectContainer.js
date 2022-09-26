import React, { useState, useEffect } from "react";
import Project from "../components/Project";
import { useMediaQuery } from "react-responsive";

import bettle1 from "../assets/BETTLE/bettle1.png";
import bettle2 from "../assets/BETTLE/bettle2.png";
import bettle3 from "../assets/BETTLE/bettle3.png";
import bettle4 from "../assets/BETTLE/bettle4.png";
import bettle5 from "../assets/BETTLE/bettle5.png";
import bettle6 from "../assets/BETTLE/bettle6.png";


import cat1 from "../assets/고양이웃/cat1.png";
import cat2 from "../assets/고양이웃/cat2.png";
import cat3 from "../assets/고양이웃/cat3.png";
import cat4 from "../assets/고양이웃/cat4.png";
import cat5 from "../assets/고양이웃/cat5.png";
import cat6 from "../assets/고양이웃/cat6.png";


import starting1 from "../assets/STARTING/starting1.png";
import starting2 from "../assets/STARTING/starting2.png";
import starting3 from "../assets/STARTING/starting3.png";
import starting4 from "../assets/STARTING/starting4.png";
import starting5 from "../assets/STARTING/starting5.png";


function ProjectContainer () {
  const projects = [
    {
      id: 1,
      name: "BETTLE 웹서비스 구현",
      info: `고대멋사 10기 해커톤 8조
      소규모 게임 배팅 서비스 'BETTLE'
      코인 배팅, 위치기반 게임 매칭 플랫폼`,
      tag: ["HTML", "CSS", "Django", "vanilla JS"],
      image: [
        bettle1,
        bettle2,
        bettle3,
        bettle4,
        bettle5,
        bettle6,
      ],
      git: "https://github.com/Park747/Hackathon8",
      mode: "web",
      role: ['Full-Stack']
    },

    {
      id: 2,
      name: "고양이웃",
      info: `서울대 x 고려대 멋사 연합해커톤 6조
      위치기반 펫 시터 매칭 플랫폼
      Kakaomap API의 Custom overlay 마커 활용
      Geolocation API를 활용하여 실시간 위치정보 활용
      기본 커뮤니티 서비스 구현`,
      tag: [
        "HTML",
        "CSS",
        "Django REST Framework",
        "Geolocation API",
        "vanilla JS",
        "Kakaomap API",
      ],
      image: [cat1, cat2, cat3, cat4, cat5],
      git: "https://github.com/CatHelp/CatHelp_Django",
      mode: "web",
      role: ['Back-end']
    },

    {
      id: 3,
      name: "STARTING",
      info: `학회, 동아리 리크루팅 플랫폼
      동아리 검색부터 지원까지 한번에
      손쉬운 지원자 관리 및 합불여부 전송
      면접 시간대까지 편하게 조율 가능한 서비스`,
      tag: [
        "React",
        "Styled Components",
        "Redux",
        "Firebase",
        "Django REST Framework",
      ],
      image: [starting1, starting2, starting3, starting4, starting5],
      git: "https://github.com/Park747/STARTING",
      mode: "app",
      role: ['Back-end']
    },
  ];

  let [mode, setMode] = useState("");

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

  return (
    <>
      <Project projects={projects} mode={mode} />
    </>
  );
}

export default ProjectContainer;
