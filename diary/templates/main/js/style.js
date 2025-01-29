document.addEventListener('DOMContentLoaded', function () {
  const username = "{{ user.username }}"; // Django 템플릿에서 사용자 이름을 가져옴

  // FullCalendar 초기화
  const calendarEl = document.getElementById('calendar');
  const calendar = new FullCalendar.Calendar(calendarEl, {
      locale: 'ko',
      headerToolbar: {
          left: 'prev,next today',
          center: 'title',
          right: 'month,basicWeek,basicDay'
      },
      initialDate: moment().format('YYYY-MM-DD'),
      editable: true,
      eventLimit: true,
      events: function (info, successCallback, failureCallback) {
          fetch(`/calendar/calendar/${username}/${info.startStr}/`)
              .then(response => response.json())
              .then(data => {
                  if (data && data.events) {
                      const events = data.events.map(event => ({
                          title: event.title,
                          start: moment(event.start_date).utcOffset(9).format('YYYY년 MM월 DD일 HH:mm'),
                          end: event.end_date ? moment(event.end_date).utcOffset(9).format('YYYY년 MM월 DD일 HH:mm') : '미정',
                          color: event.color || '#FFD700',
                          content: event.content
                      }));
                      successCallback(events);
                  }
              })
              .catch(error => {
                  console.error("Error fetching events", error);
                  failureCallback();
              });
      },
      dateClick: function (info) {
          const formattedDate = info.dateStr;
          const displayDate = info.date.toLocaleDateString('ko-KR', {
              weekday: 'long',
              year: 'numeric',
              month: 'long',
              day: 'numeric'
          });

          document.getElementById('selectedDate').innerHTML = `${info.date.toLocaleDateString('ko-KR', { weekday: 'long' })} <span>${displayDate}</span>`;

          // 해당 날짜에 맞는 일정을 가져오기
          fetch(`/calendar/calendar/${username}/${formattedDate}/`)
              .then(response => response.json())
              .then(data => {
                  const eventList = document.querySelector('.eventList');
                  eventList.innerHTML = '';  // 기존 일정 목록 비우기

                  if (data && data.events) {
                      data.events.forEach(event => {
                          const startDate = moment(event.start_date).utcOffset(9).format('YYYY년 MM월 DD일 HH:mm');
                          const endDate = event.end_date ? moment(event.end_date).utcOffset(9).format('YYYY년 MM월 DD일 HH:mm') : '미정';
                          const eventItem = document.createElement('li');
                          eventItem.id = `event-${event.id}`;
                          eventItem.classList.add('event-card');
                          eventItem.innerHTML = `
                              <div class="event-header" style="background-color: ${event.color};">
                                  <strong class="event-title">${event.title}</strong>
                                  <span class="event-time">${startDate} ~ ${endDate}</span>
                              </div>
                              <div class="event-body">
                                  <p class="event-description">${event.content}</p>
                              </div>
                          `;
                          eventList.appendChild(eventItem);
                      });
                  } else {
                      eventList.innerHTML = '<li>일정이 없습니다.</li>';
                  }
              })
              .catch(error => {
                  console.error("Error fetching events for selected date", error);
              });
      }
  });

  calendar.render();

  // 일정 추가 처리
  const addEventForm = document.getElementById('addEventForm');
  addEventForm.addEventListener('submit', function (e) {
      e.preventDefault();

      const taskName = document.getElementById('taskName').value;
      const taskDescription = document.getElementById('taskDescription').value;
      const startDate = document.getElementById('startDate').value;
      const startTime = document.getElementById('startTime').value;
      const endDate = document.getElementById('endDate').value;
      const endTime = document.getElementById('endTime').value;
      const taskColor = document.getElementById('taskColor').value;

      // 유효성 검사 추가
      if (!taskName || !startDate || !startTime) {
          alert('일정 이름, 시작일, 시작 시간을 모두 입력해주세요.');
          return;
      }

      fetch('/calendar/add_event/', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': '{{ csrf_token }}' // CSRF 토큰 헤더 추가
          },
          body: JSON.stringify({
              title: taskName,
              content: taskDescription,
              start_date: `${startDate}T${startTime}`,
              end_date: `${endDate}T${endTime}`,
              color: taskColor
          })
      })
      .then(response => response.json())
      .then(data => {
          if (data.success) {
              alert('일정이 추가되었습니다.');
              $('#addEventModal').modal('hide');
              calendar.refetchEvents(); // 새로운 이벤트를 다시 불러오기
          } else {
              alert('일정 추가에 실패했습니다.');
          }
      })
      .catch(() => {
          alert('일정 추가 실패');
      });
  });
});
