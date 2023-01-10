// create a basic sllideshow application in rect JS
function Slides({ slides }) {


  const [activeSlideNo, setActiveSlideNo] = useState(0);
  const [currentSlide, setCurrentSlide] = useState(slides[0]);
  const [disablePrev, setDisablePrev] = useState(true);
  const [disableNext, setDisableNext] = useState(true);
  const [disableRestart, setDisableRestart] = useState(true);

  const onClickNext = () => {
    let curSlideNo = activeSlideNo;
    if (curSlideNo < slides.length - 1) {
      curSlideNo++;
      setActiveSlideNo(curSlideNo);
      setCurrentSlide(slides[curSlideNo]);
      setDisablePrev(false);
      setDisableRestart(false);
    }

    if (curSlideNo == slides.length - 1) {
      setdisableNext(true);
    }
  };

  const onClickPrev = () => {
    let curSlideNo = activeSlideNo;
    if (curSlideNo > 0) {
      curSlideNo--;
      setActiveSlideNo(curSlideNo);
      setCurrentSlide(slides[curSlideNo]);
      setDisableNext(false);
    }

    if (curSlideNo == 0) {
      setdisablePrev(true);
      setDisableRestart(true);
    }
  };

  const onClickRestart = () => {
    setActiveSlideNo(0);
    setCurrentSlide(slides[0]);
    setDisableNext(false);
    setdisablePrev(true);
    setDisableRestart(true);
  };

  return (
    <div>
      <div id="navigation" className="text-center">
        <button disabled={disableRestart} onClick={() => onClickRestart()}>Restart</button>
        <button disabled={disablePrev} onClick={() => onClickPrev()}>Prev</button>
        <button disabled={disableNext} onClick={() => onClickNext()}>Next</button>
      </div>
    </div>
  );
}
