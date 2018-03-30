import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { TestService } from '../../services/test.service';
import { Project } from '../../model/project';
import { Weather } from '../../model/weather';

@Component({
  selector: 'app-wit',
  templateUrl: './wit.component.html',
  styleUrls: ['./wit.component.css']
})
export class WitComponent implements OnInit {
  sprint: string;
  added: string;
  projects: Project[];
  selectedProject: string;
  weather: Weather;

  constructor(
    private testService: TestService
  ) { }

  ngOnInit() {
    this.sprint = '';
    this.weather = {
      response: {},
      current_observation: {
        temp_f: -1,
        temp_c: -1,
        weather: '',
        feelslike_f: '',
        feelslike_c: ''
      }
    }
    this.weather.current_observation.weather = '';
    this.weather.current_observation.feelslike_f = '';
    this.testService.getProjects().subscribe(
      res => this.test(res)
    );

    this.testService.getWeather('Kaysville').subscribe(
      res => this.weather = res
    );
  }

  test(res: Project[]) {
    this.projects = res;
  }

  addTraining(): void {
    let sprintObj: Object = {
      sprint: this.sprint,
      project: this.selectedProject
    }
    this.testService.addTraining(sprintObj).subscribe(
      res => this.successAdd(res)
    )

  }

  successAdd(res: Object): void {
    this.added = 'Training Added!'
    setTimeout(() => {
      this.added = '';
    }, 5000);
  }
}
