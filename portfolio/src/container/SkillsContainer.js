import React from "react";
import Skills from "../components/Skills";

import reactIcon from "../assets/skills/react.png";
import htmlIcon from "../assets/skills/html.png";
import cssIcon from "../assets/skills/css.png";
import jsIcon from "../assets/skills/js.png";
import scIcon from "../assets/skills/styled-components.png";
import gitIcon from "../assets/skills/git.png";
import pyIcon from "../assets/skills/python.png";
import fbIcon from "../assets/skills/firebase.png";
import sassIcon from "../assets/skills/sass.png";
import bsIcon from "../assets/skills/bootstrap.png";
import djIcon from "../assets/skills/django.png";


function SkillsContainer() {
  const skills = [
    { name: "HTML", icon: htmlIcon },
    { name: "CSS", icon: cssIcon },
    { name: "JavaScript", icon: jsIcon },
    { name: "Sass", icon: sassIcon },
    { name: "React", icon: reactIcon },
    { name: "styled-components", icon: scIcon },
    { name: "Bootstrap", icon: bsIcon },
    { name: "Git", icon: gitIcon },
    { name: "Python", icon: pyIcon },
    { name: "Firebase", icon: fbIcon },
    { name: "Django", icon: djIcon},
  ];
  return <Skills skills={skills} />;
}

export default SkillsContainer;
