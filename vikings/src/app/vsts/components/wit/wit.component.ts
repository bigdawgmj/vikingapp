import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { TestService } from '../../services/test.service';
import { Project } from '../../model/project';

@Component({
  selector: 'app-wit',
  templateUrl: './wit.component.html',
  styleUrls: ['./wit.component.css']
})
export class WitComponent implements OnInit {
  sprint: string;
  added: string;
  projects: Project[]
  selectedProject: string

  constructor(
    private testService: TestService
  ) { }

  ngOnInit() {
    this.sprint = '';
    this.testService.getProjects().subscribe(
      res => this.test(res)
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
