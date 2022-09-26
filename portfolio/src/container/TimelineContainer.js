import React, { useState, useEffect } from "react";
import Timeline from "../components/Timeline";

import { useMediaQuery } from "react-responsive";

function TimelineContainer({ sidebar, setSidebar }) {
  const isPc = useMediaQuery({
    query: "(min-width:768px)",
  });
  const isMobile = useMediaQuery({
    query: "(max-width:767px)",
  });
  const timeLine = [
    {
      id: 0,
      date: "2018.02 - present",
      title: "Korea University",
      content: "고려대학교 보건과학대학 입학",
      category: "univ",
    },

    {
      id: 1,
      date: "2018.03 - 2018.12",
      title: "보건환경융합과학부 총학생회",
      content:
        "보건환경융합과학부 총학생회 기획국원으로 활동함",
      category: "univ2",
    },

    {
      id: 2,
      date: "2018.05 - present",
      title: "TTP",
      content: "고려대학교 중앙피아노동아리 TTP 가입",
      category: "ttp",
    },

    {
      id: 3,
      date: "2018.09 - 2019.06",
      title: "clo.Z",
      content:
        "고려대학교 중앙패션동아리 clo.Z 가입",
      category: "cloZ",
    },

    {
      id: 4,
      date: "2020.03 - 2021.09",
      title: "Military Service",
      content:
        "대한민국 육군 8군수지원단 병장 만기전역",
      category: "Army",
    },

    {
      id: 5,
      date: "2021.09 - 2021.12",
      title: "2022학년도 수능 재도전",
      content:
        "개같이 멸망",
      category: "mentor",
    },

    {
      id: 6,
      date: "2022.01 - 2022.06",
      title: "ICT EHS Lab",
      content: "고려대 ICT 환경안전보건 연구실 인턴",
      category: "lab",
    },

    {
      id: 7,
      date: "2022.05 - present",
      title: "KOSHA reporters",
      content:
        "안전보건공단 기자단원 활동",
      category: "mentor",
    },

    {
      id: 8,
      date: "2022.03 - present",
      title: "NEXT x Likelion",
      content:
        "고려대학교 소프트웨어벤처 학회 NEXT x 멋쟁이사자처럼 10기 합격",
      category: "mentor",
    },

    {
      id: 9,
      date: "2022.05",
      title: "고대 멋사 10기 해커톤",
      content:
        "혼돈의 첫 해커톤, BETTLE 프로젝트",
      category: "project",
    },

    {
      id: 10,
      date: "2022.08",
      title: "서울대 고려대 연합 해커톤",
      content:
        "고양이웃 프로젝트 백엔드 구현",
      category: "project",
    },

    {
      id: 11,
      date: "2022.07 ~ present",
      title: "STARTING Project",
      content: "동아리,학회 종합 리크루팅 웹서비스 구현 project",
      category: "project",
    },
  ];

  const [mode, setMode] = useState("");

  useEffect(() => {
    if (isPc) setMode("isPc");
    else if (isMobile) setMode("isMobile");
  }, [isMobile, isPc]);

  return (
    <Timeline
      sidebar={sidebar}
      setSidebar={setSidebar}
      timeLine={timeLine}
      mode={mode}
    />
  );
}

export default TimelineContainer;
