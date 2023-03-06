# import googletrans
# from googletrans import Translator

# print(googletrans.LANGUAGES)

# text1 = "Hello welcome to my website!"
# tr = Translator()
# print(tr.detect(text1))
# trans1 = tr.translate(text1, src='en', dest='ja')
# print("English to Japanese: ", trans1.text)

# 1. 번역전 문장, 나라코드들이 유지되도록
# 2. 체인지 기능도 달아주세요 ~
# 3. 하실 수 있으시면 처음에 접근했을 때 출발지(영어), 목적지(한국어) 세팅


# 문자열대로 읽어줌
# https://pypi.org/project/gTTS/
# pip install gTTS 설치
from gtts import gTTS
tts = gTTS('안녕하세요', lang="ko")
tts.save('media/hello.mp3')
# url로부터 그나마 자유로운 media에!


# 3/2 vote 자료 자바스크립트 제공
# =====================================================================================================================
# VOTE/INDEX
# =====================================================================================================================

# <h1><b>투표소</b></h1>

# <div class="text-end">
#     <a href="# class="btn btn-dark btn-lg">+TOPIC</a>
# </div>

# <div class="row">

#     <div class="col-sm-4">
#         <div class="card text-center">
#             <img src="#" class="card-img-top" alt="...">
#             <div class="card-body" {% if user in i.voter.all %} style="background-color: rgb(250, 235, 215);" {% endif %}>
#                 <h4 class="card-title"><b>2</b></h4>
#                 <p class="card-text">3</p>
#                 <a href="#" class="btn btn-outline-dark">
#                     투표하기
#                     <!-- 투표한사람들에게는 결과보기로 띄워주기 -->
#                 </a>
#                 <button type="button" class="btn btn-outline-danger" data-bs-toggle="modal" data-bs-target="#e{{forloop.counter}}">
#                     삭제하기
#                 </button>
#                 <!-- 투표를 만든사람한테만 삭제하기가 보이도록 -->
#             </div>
#         </div>
#     </div>

# </div>

# <!-- Modal -->
# <div class="modal fade" id="e{{forloop.counter}}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
#     <div class="modal-dialog">
#         <div class="modal-content">
#             <div class="modal-header">
#                 <h1 class="modal-title fs-5" id="exampleModalLabel"><b>{{ i.subject }}</b> 토픽 삭제 알림창</h1>
#                 <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
#             </div>
#             <div class="modal-body">
#                 <mark><b>0</b></mark>명이 참여한 투표입니다. 그래도 삭제하시겠습니까?
#             </div>
#             <div class="modal-footer">
#                 <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">창 닫기</button>
#                 <a href="#" type="button" class="btn btn-danger">삭제하기</a>
#             </div>
#         </div>
#     </div>
# </div>




# =====================================================================================================================
# VOTE/DETAIL
# =====================================================================================================================
# <h1><b>주제</b></h1>


# <div class="row mt-4">
#     <div class="col-sm-9">
#         <textarea class="form-control" style="height:250px" disabled>설명</textarea>
#     </div>
#     <div class="col-sm-3">
#         <img src="#" width="100%">
#         <div class="mt-3 text-center">
#             <h4>made by <b>작성자</b></h4>
#         </div>
#     </div>
# </div>

# <hr>

# <!-- 투표를 한사람이라면 -->
#     <!-- <div class="row mt-5">
        
#         <div class="col-sm-4">
#             <label class="form-check-label">
#                 <h4><b>이름</b></h4>
#             </label>
#             <div class="progress mt-3 mb-3" role="progressbar" aria-label="Animated striped example" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
#                 <div class="progress-bar progress-bar-striped progress-bar-animated" style="width: {{ i.choicer.count|div:t.voter.count|mul:100|floatformat:2 }}%">{{ i.choicer.count|div:t.voter.count|mul:100|floatformat:2 }} %</div>
#             </div>
#             <textarea class="form-control mt-3" style="height: 100px;" disabled>보기설명</textarea>
#         </div>
        
#     </div>
#     <div class="text-end mt-4">
#         <a href="{% url 'vote:cancel' t.id %}" class="btn btn-danger">무르기</a>
#     </div> -->



# <!-- 투표를 한사람이 아니라면 -->
# <div class="row mt-5">
#     <div class="col-sm-4">
#         <input type="radio" class="form-check-input">
#         <label class="form-check-label">
#             <h4><b>보기이름</b></h4>
#         </label>
#         <textarea class="form-control mt-3" style="height: 100px;" disabled>보기설명</textarea>
#     </div>
# </div>
# <div class="text-end mt-4">
#     <button class="btn btn-dark">투표하기</button>
# </div>







# =====================================================================================================================
# VOTE/create
# =====================================================================================================================
# <h1><b>토픽생성</b></h1>

# <input type="text" placeholder="INPUT SUBJECT" class="form-control mt-5">
# <input type="text" value="{{user}}" disabled class="form-control mt-3 mb-3">
# <textarea class="form-control" style="height: 200px;" placeholder="INPUT CONTENT"></textarea>

# <div class="text-end mt-4">
#     <button type="button" onclick="makecho()" class="btn btn-dark">보기생성</button>
#     <button class="btn btn-dark">토픽생성</button>
# </div>

# <div id="here" class="row mt-5"></div>


# <script>
#     function makecho(){
#         d = document.getElementById("here");
#         n = document.createElement("div");
#         n.setAttribute("class", "col-sm-4");
#         n.innerHTML = "<input type='text' placeholder='INPUT NAME' class='form-control'>\
#         <textarea class='form-control mt-3 mb-5' placeholder='INPUT COMMENT'></textarea>";
#         d.appendChild(n);
#     }
# </script>




# 3/3
# <h1><b>BOOK PAGE</b></h1>

# <div class="text-end">
#     <a href="#" class="btn btn-success"> + BOOKMARK </a>
# </div>

# <div class="row">
#     <div class="col-sm-4 mb-3 mb-sm-0 mt-4">
#         <div class="card">
#             <div class="card-body" style="background-color: antiquewhite;">
#                 <h5 class="card-title"><b>사이트이름</b></h5>
#                 <p class="card-text">사이트요약</p>
#                 <a href="#" class="btn btn-primary">사이트이동</a>
#             </div>
#         </div>
#     </div>
# </div>


# =======================================
# book/create.html
# =======================================

# <h1><b>북마크생성</b></h1>

# <div class="text-end">
#     <input type="checkbox" class="btn-check" id="btn-check-outlined" autocomplete="off">
#     <label class="btn btn-outline-warning" for="btn-check-outlined">✨</label><br>
# </div>
# <input type="text" placeholder="사이트 이름을 입력하세요" class="form-control mt-3">
# <input type="text" placeholder="사이트 URL 을 입력하세요" class="form-control mt-4 mb-4">
# <textarea class="form-control" placeholder="사이트를 간략하게 설명해주세요" style="height: 100px;"></textarea>

# <div class="text-end mt-5">
#     <button class="btn btn-dark">생성</button>
# </div>

# TTS
# text to speech
# 문자열을 입력하면 읽어주는 서비스!