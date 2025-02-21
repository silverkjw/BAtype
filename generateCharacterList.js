const fs = require("fs");
const path = require("path");

const imagesDir = path.join(__dirname, "images"); // images 폴더 경로
const outputFile = path.join(__dirname, "characters.js"); // 출력될 JS 파일 경로

fs.readdir(imagesDir, (err, files) => {
    if (err) {
        console.error("이미지 폴더를 읽는 중 오류 발생:", err);
        return;
    }

    // .png 파일만 필터링
    let imageFiles = files.filter(file => file.endsWith(".png"));

    // 카테고리별로 분류할 객체 생성
    let categories = {};

    imageFiles.forEach(file => {
        let [category, name] = file.replace(".png", "").split(",");
        if (!categories[category]) {
            categories[category] = [];
        }
        categories[category].push(name);
    });

    // JavaScript 파일 형태로 변환
    let jsContent = `const characterData = ${JSON.stringify(categories, null, 4)};`;

    // characters.js 파일로 저장
    fs.writeFileSync(outputFile, jsContent, "utf8");
    console.log("characters.js 파일이 생성되었습니다!");
});
